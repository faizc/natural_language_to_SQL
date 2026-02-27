import pyodbc

server = "104.211.115.185"
database = "AMDATA"
username = ""
password = ""
driver = "{ODBC Driver 18 for SQL Server}"

## Following connection string format worked for me - using SQL Server driver instead of ODBC Driver 18
conn_str = (
    f'Driver={driver};'
    f'Server={server};'
    f'Database={database};'
    f'UID={username};'
    f'PWD={password};TrustServerCertificate=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
print(row)

cursor.close()
conn.close()