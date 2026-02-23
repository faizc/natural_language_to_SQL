import pandas as pd
import json 
file_path = "data/RIL_Table_Metadata.xlsx"

# Read all sheets into a dictionary
sheets_dict = pd.read_excel(
    file_path,
    sheet_name=None,        # Read all sheets
    engine="openpyxl"
)

# Iterate tab-wise
for sheet_name, df in sheets_dict.items():
    print(f"\nProcessing sheet: {sheet_name}")
#    print(df.head())

def populate_table_info(df):
    tableDesc=[]
    for row in df.itertuples(index=False):
        tableDesc.append({'TableName':row.TableName,'Description':row.Description,'Domain':row.Domain})
    return tableDesc    

def get_table_desc(table_info, tablename):
    table_comment = None
    for table in table_info:
        if table["TableName"] == tablename:
            table_comment = table["Description"]
            break  
    return table_comment    

def populate_column_info(df, table_info, tablename, globalStructure):
    globalStructure=[]
    columnDesc=[]
    for row in df.itertuples(index=False):
        columnDesc.append({'ColumnName':row.ColumnName,'Description':row.Description, 'DataType':row.DataType})
    # Add the last column description array to the global structure. 
    globalStructure.append({'TableName':tablename, 'Description':get_table_desc(table_info, tablename), 'Columns':columnDesc})

    return globalStructure

table_info = populate_table_info(df)
#print(table_info)

file_path = "data/RIL_Table_Columns_Metadata.xlsx"
tableColumnStructure=[]

for table in table_info:
    #print(table["TableName"], table["Description"], table["Domain"])
    # Read all sheets into a dictionary
    sheets_dict = pd.read_excel(
        file_path,
        sheet_name=table["TableName"],   # Read specific sheet based on table name
        engine="openpyxl"
    )
    #print(sheets_dict.head())
    tableColumnStructure.append(populate_column_info(sheets_dict, table_info, table["TableName"], tableColumnStructure)[0])

#print(json.dumps(tableColumnStructure, indent=4))

with open("data/table_column_info.json", "w", encoding="utf-8") as f:
    json.dump(tableColumnStructure, f, indent=4)

with open("data/table_info.json", "w", encoding="utf-8") as f:
    json.dump(table_info, f, indent=4)
