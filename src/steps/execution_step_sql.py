import sys
import os
sys.path.append("../../")
import json
from rich.console import Console
from semantic_kernel.processes.kernel_process import KernelProcessStep, KernelProcessStepContext
from semantic_kernel.kernel import Kernel
from semantic_kernel.functions import kernel_function

from src.models.events import SQLEvents
from src.models.step_models import ExecutionStepInput, Execution2TableNames
from src.utils.step_tracker import get_tracker

import pyodbc
import datetime
import decimal
console = Console()

class ExecutionStepSQL(KernelProcessStep):
    """Execute SQL statement and emit appropriate event."""
    @kernel_function(name="execute_sql")
    async def execute_sql(self, context: KernelProcessStepContext, data: ExecutionStepInput, kernel: Kernel):
        # Start tracking this step
        tracker = get_tracker()
        tracker.start_step("ExecutionStepSQL", data)
        
        print("Running ExecutionStepSQL...")
        print(f"SQL statement to execute: {data.sql_statement}")

        try:
            server = os.environ.get("SQL_SERVER_HOST")
            database = os.environ.get("SQL_SERVER_DATABASE")
            username = os.environ.get("SQL_SERVER_USERNAME")
            password = os.environ.get("SQL_SERVER_PASSWORD")

            conn_str = (
                f'Driver={{SQL Server}};'
                f'Server={server};'
                f'Database={database};'
                f'UID={username};'
                f'PWD={password};'
            )
            response = None
            columns = []
            with pyodbc.connect(conn_str) as conn:
                cur = conn.cursor()
                cur.execute(data.sql_statement)

                response = cur.fetchall()   # <-- ONE variable holding all rows

                columns = [col[0] for col in cur.description]
                cur.close()

            console.print(response)
            print("SQL execution succeeded.")


            def json_default(o):
                if isinstance(o, (datetime.date, datetime.datetime)):
                    return o.isoformat()
                if isinstance(o, decimal.Decimal):
                    return float(o)
                return str(o)   # final fallbac


            json_response = [
                dict(zip(columns, row))
                for row in response
            ]

            resp_dd = {"query": data.user_query, "response": json_response}

            console.print("resp_dd", resp_dd)

            try:
                with open("response.json", "w") as f:
                    json.dump(resp_dd, f, indent=4)
            except Exception as e:
                console.print(f"[red]Error writing response to file: {str(e)}[/red]")

            print("Emitted event: ExecutionSuccess.")
            await context.emit_event(process_event=SQLEvents.ExecutionSuccess, data=response)
            
            # End tracking with process completion
            tracker.end_step(next_step="Process End", next_event=SQLEvents.ExecutionSuccess, output_data=response)

        except Exception as e:
            error_description = f"Execution error: {str(e)}"
            result = Execution2TableNames(
                user_query=data.user_query,
                table_names=data.table_names,
                column_names=data.column_names,
                sql_statement=data.sql_statement,
                error_description=error_description
            )
            await context.emit_event(process_event=SQLEvents.ExecutionError, data=result)
            resp_dd = {"query": data.user_query, "response": error_description}
                
            with open("response.json", "w") as f:
                json.dump(resp_dd, f, indent=4)
            print("Emitted event: ExecutionError.")
            
            # End tracking with error transition back to TableNameStep
            tracker.end_step(next_step="TableNameStep", next_event=SQLEvents.ExecutionError, output_data=result)