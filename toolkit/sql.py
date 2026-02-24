#nl2sql-sindia-001.database.windows.net

import pyodbc

server = "104.211.115.185"
database = "AMDATA"
username = ""
password = ""
driver = "{ODBC Driver 18 for SQL Server}"

conn_str = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
)

conn_str = (
    f"DRIVER={'SQL Server'};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"USER={username};"
    f"PASSWORD={password};"
)

## Following connection string format worked for me - using SQL Server driver instead of ODBC Driver 18
conn_str = (
    f'Driver={{SQL Server}};'
    f'Server={server};'
    f'Database={database};'
    f'UID={username};'
    f'PWD={password};'
)

#conn = pyodbc.connect(conn_str)
#cursor = conn.cursor()
#cursor.execute("SELECT @@VERSION")
#row = cursor.fetchone()
#print(row)


#cursor.close()
#conn.close()

response = None
with pyodbc.connect(conn_str) as conn:
    cur = conn.cursor()
    cur.execute("SELECT lPortfolioItemId, CMDBId, AssetTag, lDeviceId, ril_lUserId, lSupervId, AMModel_lParentId, Hostname, IPAddress, Related_IP,     all_ip, ril_console_ip, computertype, operatingsystem, OS_Version, Asset_SerialNo, ModelName, Make, location, d_Location, Owner, CoOwner,   RilAssetCategory, RilEnvZone, RIL_ManagedBy, RIL_Functional_Group, d_DeviceType, d_ServerType, d_OSwise, d_Environmentwise FROM    AMDATA.dbo.con_am_asset_lifecycle")
    
    response = cur.fetchall()   # <-- ONE variable holding all rows

    cur.close()

print(response)
