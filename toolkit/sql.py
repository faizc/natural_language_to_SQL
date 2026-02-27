#nl2sql-sindia-001.database.windows.net

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

response = None
with pyodbc.connect(conn_str) as conn:
    cur = conn.cursor()
    cur.execute("SELECT lPortfolioItemId, CMDBId, AssetTag, lDeviceId, ril_lUserId, lSupervId, AMModel_lParentId, Hostname, IPAddress, Related_IP,     all_ip, ril_console_ip, computertype, operatingsystem, OS_Version, Asset_SerialNo, ModelName, Make, location, d_Location, Owner, CoOwner,   RilAssetCategory, RilEnvZone, RIL_ManagedBy, RIL_Functional_Group, d_DeviceType, d_ServerType, d_OSwise, d_Environmentwise FROM    AMDATA.dbo.con_am_asset_lifecycle")
    
    response = cur.fetchall()   # <-- ONE variable holding all rows

    cur.close()

print(response)
