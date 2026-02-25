table_descriptions = [
    {
        "TableName": "AM",
        "Description": "Asset Management is a Enterprise level tool that tracks and manage the lifecycle of Assets like VM Server, Physical Server, IP Phones, Switch routers. helps organizations track, control, and optimize their IT assets across the full lifecycle",
        "Domain": "[AMDATA].[dbo].[con_am_asset_lifecycle]"
    },
    {
        "TableName": "Monitoring",
        "Description": "This tool is used by IT and operations teams to track, monitor, and manage the health, availability, and performance of IT assets across an organization.",
        "Domain": "[Monitoring].[dbo].[Monitoring]"
    },
    {
        "TableName": "BKP_Inventory",
        "Description": "Veritas Netbackup - enterprise-grade backup and recovery solution used by organizations to protect, manage, and recover data across complex IT environments.",
        "Domain": "[BKP_Inventory].[dbo].[BKP_Inventory]"
    },
    {
        "TableName": "BKP_Logs",
        "Description": "enterprise-grade backup and recovery solution used by organizations to protect, manage, and recover data across complex IT environments..Backup Inventory Log Information",
        "Domain": "[BKP_Logs].[dbo].[BKP_Logs]"
    },
    {
        "TableName": "SLA_ClosedTKT",
        "Description": "It\u2019s an IT Service Management (ITSM) ticketing tool used by IT teams to log, track, and manage service-related work across an organization.",
        "Domain": "[HPSM_Tickets].[dbo].[SLA_ClosedTKT]"
    },
    {
        "TableName": "CR_Asset",
        "Description": "Change Management tickets which contains CI names",
        "Domain": "[HPSM_Tickets].[dbo].[CR_Asset]"
    }
]


json_rules = """
  "rules": [
  ]
"""


global_database_model = [
    {
        "TableName": "AM",
        "Domain": "[AMDATA].[dbo].[con_am_asset_lifecycle]",
        "Description": "Asset Management is a Enterprise level tool that tracks and manage the lifecycle of Assets like VM Server, Physical Server, IP Phones, Switch routers. helps organizations track, control, and optimize their IT assets across the full lifecycle",
        "Columns": [
            {
                "ColumnName": "lPortfolioItemId",
                "Description": "Unique identifier for portfolio item of Asset",
                "DataType": "Number"
            },
            {
                "ColumnName": "CMDBId",
                "Description": "Configuration Management Database ID which comes from uCMDB tool after auto discovery",
                "DataType": "Text"
            },
            {
                "ColumnName": "AssetTag",
                "Description": "Physical asset tag number",
                "DataType": "Text"
            },
            {
                "ColumnName": "lDeviceId",
                "Description": "Unique device identifier",
                "DataType": "Number"
            },
            {
                "ColumnName": "RilAssetCategory",
                "Description": "Asset category classification (e.g., CRITICAL)",
                "DataType": "Text"
            },
            {
                "ColumnName": "RilEnvZone",
                "Description": "Environment zone (e.g., INTRANET, DMZ)",
                "DataType": "Text"
            },
            {
                "ColumnName": "ril_cidc_support_PS",
                "Description": "CIDC support for Production Support",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_lUserId",
                "Description": "User ID of the assigned user",
                "DataType": "Number"
            },
            {
                "ColumnName": "RIL_ManagedBy",
                "Description": "Name of the managing group/person",
                "DataType": "Text"
            },
            {
                "ColumnName": "ril_managedby_email1",
                "Description": "Primary email of managing contact",
                "DataType": "Email"
            },
            {
                "ColumnName": "ril_managedby_phone1",
                "Description": "Primary phone of managing contact",
                "DataType": "Text"
            },
            {
                "ColumnName": "ril_managedby_email2",
                "Description": "Secondary email of managing contact",
                "DataType": "Email"
            },
            {
                "ColumnName": "ril_managedby_email3",
                "Description": "Tertiary email of managing contact",
                "DataType": "Email"
            },
            {
                "ColumnName": "ril_managedby_email4",
                "Description": "Quaternary email of managing contact",
                "DataType": "Email"
            },
            {
                "ColumnName": "ril_managedby_phone2",
                "Description": "Secondary phone of managing contact",
                "DataType": "Text"
            },
            {
                "ColumnName": "RIL_Functional_Group",
                "Description": "Functional group responsible for asset.It explains the Functional Group to which the Asset belongs to",
                "DataType": "Text"
            },
            {
                "ColumnName": "RIL_IDCSupport_Backup",
                "Description": "IDC backup support availability flag",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_application_name",
                "Description": "Name of the hosted application",
                "DataType": "Text"
            },
            {
                "ColumnName": "ril_console_ip",
                "Description": "Console IP address of the device",
                "DataType": "IP Address"
            },
            {
                "ColumnName": "RIL_Top_Biz_List",
                "Description": "Top business list categorization",
                "DataType": "Text"
            },
            {
                "ColumnName": "RIL_IDC_UFactor",
                "Description": "IDC U-factor (rack unit size)",
                "DataType": "Text/Number"
            },
            {
                "ColumnName": "ril_idc_support_SAN",
                "Description": "IDC support for SAN",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_cidc_support_DB",
                "Description": "CIDC support for Database",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_cidc_support_HW",
                "Description": "CIDC support for Hardware",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_cidc_support_NW",
                "Description": "CIDC support for Network",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_cidc_support_OSA",
                "Description": "CIDC support for OS Administration",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "ril_cidc_support_APP",
                "Description": "CIDC support for Application",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "computertype",
                "Description": "Type of computer (e.g., Virtual Machine, Physical)",
                "DataType": "Text"
            },
            {
                "ColumnName": "operatingsystem",
                "Description": "Operating system name and version",
                "DataType": "Text"
            },
            {
                "ColumnName": "IPAddress",
                "Description": "Primary IP address of the device",
                "DataType": "IP Address"
            },
            {
                "ColumnName": "Hostname",
                "Description": "Network hostname of the device",
                "DataType": "Text"
            },
            {
                "ColumnName": "Asset_SerialNo",
                "Description": "Hardware serial number of the asset",
                "DataType": "Text"
            },
            {
                "ColumnName": "ModelName",
                "Description": "Model name of the hardware",
                "DataType": "Text"
            },
            {
                "ColumnName": "Make",
                "Description": "Manufacturer/make of the hardware",
                "DataType": "Text"
            },
            {
                "ColumnName": "location",
                "Description": "Physical location/rack location of asset",
                "DataType": "Text"
            },
            {
                "ColumnName": "Owner",
                "Description": "Asset owner name",
                "DataType": "Text"
            },
            {
                "ColumnName": "lSupervId",
                "Description": "Supervisor/approver user ID",
                "DataType": "Number"
            },
            {
                "ColumnName": "AMPORTFOLIO_RIL_IDC_Inv_Biz_List",
                "Description": "IDC inventory business list for AM Portfolio",
                "DataType": "Text"
            },
            {
                "ColumnName": "PS_ContactName",
                "Description": "Production Support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "NW_ContactName",
                "Description": "Network support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "OSA_ContactName",
                "Description": "OS Administration contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "APP_ContactName",
                "Description": "Application support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "DB_ContactName",
                "Description": "Database support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "SAN_ContactName",
                "Description": "SAN support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "Backup_ContactName",
                "Description": "Backup support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "CoOwner",
                "Description": "Co-owner of the asset",
                "DataType": "Text"
            },
            {
                "ColumnName": "User_HOD",
                "Description": "Head of Department of the asset user",
                "DataType": "Text"
            },
            {
                "ColumnName": "HW_ContactName",
                "Description": "Hardware support contact name",
                "DataType": "Text"
            },
            {
                "ColumnName": "AMModel_lParentId",
                "Description": "Parent ID in AM model hierarchy",
                "DataType": "Number"
            },
            {
                "ColumnName": "d_OSwise",
                "Description": "Derived field - OS classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_Location",
                "Description": "Derived field - Location classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_Support_Function",
                "Description": "Derived field - Support function type",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_ServerType",
                "Description": "Derived field - Server type classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_Environmentwise",
                "Description": "Derived field - Environment classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "os_eol_date",
                "Description": "Operating system End of Life date",
                "DataType": "Date"
            },
            {
                "ColumnName": "os_eos_date",
                "Description": "Operating system End of Support date",
                "DataType": "Date"
            },
            {
                "ColumnName": "hw_eol_date",
                "Description": "Hardware End of Life date",
                "DataType": "Date"
            },
            {
                "ColumnName": "hw_eos_date",
                "Description": "Hardware End of Support date",
                "DataType": "Date"
            },
            {
                "ColumnName": "OSServiceLevel",
                "Description": "Operating system service level",
                "DataType": "Text"
            },
            {
                "ColumnName": "MemCommentPort",
                "Description": "Memory comment / port information",
                "DataType": "Text"
            },
            {
                "ColumnName": "MemCommentLoc",
                "Description": "Memory comment / location information",
                "DataType": "Text"
            },
            {
                "ColumnName": "Related_IP",
                "Description": "Additional/related IP addresses (comma-separated)",
                "DataType": "Text"
            },
            {
                "ColumnName": "OS_Version",
                "Description": "Specific OS version string",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_DeviceType",
                "Description": "Derived field - Device type classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_OS_EOL_ageing",
                "Description": "Derived field - OS EOL ageing status",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_OS_EOS_ageing",
                "Description": "Derived field - OS EOS ageing status",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_HW_EOL_ageing",
                "Description": "Derived field - Hardware EOL ageing status",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_HW_EOS_ageing",
                "Description": "Derived field - Hardware EOS ageing status",
                "DataType": "Text"
            },
            {
                "ColumnName": "all_ip",
                "Description": "All IP addresses associated with the asset",
                "DataType": "Text"
            },
            {
                "ColumnName": "PIM_Onboarding",
                "Description": "PIM onboarding status flag",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "OBR_Onboarding",
                "Description": "OBR onboarding status flag",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "BackupYesNo",
                "Description": "Backup enabled flag",
                "DataType": "Text (YES/NO)"
            },
            {
                "ColumnName": "BackupContact",
                "Description": "Backup contact person name",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_RIL_PROV_DATE",
                "Description": "Derived field - RIL provisioning date",
                "DataType": "DateTime"
            }
        ]
    },
    {
        "TableName": "Monitoring",
        "Domain": "[Monitoring].[dbo].[Monitoring]",
        "Description": "This tool is used by IT and operations teams to track, monitor, and manage the health, availability, and performance of IT assets across an organization.",
        "Columns": [
            {
                "ColumnName": "dsi_key_id",
                "Description": "Unique device/server identifier key from DSI system",
                "DataType": "Number"
            },
            {
                "ColumnName": "dns_name",
                "Description": "Fully Qualified Domain Name (FQDN) of the server",
                "DataType": "Text"
            },
            {
                "ColumnName": "host_name",
                "Description": "hostname of the server (without domain suffix)",
                "DataType": "Text"
            },
            {
                "ColumnName": "NODE_ta_period",
                "Description": "Date Time aggregation period for the node metrics (yyyy-mm-dd hh:mm.s format)",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "totUpTime",
                "Description": "Total uptime of the server in minutes during the period",
                "DataType": "Number (Minutes)"
            },
            {
                "ColumnName": "totDowntime",
                "Description": "Total unplanned downtime in minutes during the period",
                "DataType": "Number (Minutes)"
            },
            {
                "ColumnName": "totPlanDTime",
                "Description": "Total planned downtime in minutes during the period",
                "DataType": "Number (Minutes)"
            },
            {
                "ColumnName": "totExcDTime",
                "Description": "Total excluded downtime in minutes during the period",
                "DataType": "Number (Minutes)"
            },
            {
                "ColumnName": "D_Avail_Perc",
                "Description": "Derived column to calculate Availability percentage for the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "dsi_key_id_",
                "Description": "ID",
                "DataType": "Number"
            },
            {
                "ColumnName": "ta_period",
                "Description": "Date Time aggregation period for the node metrics (yyyy-mm-dd hh:mm.s format)",
                "DataType": "Text (Time)"
            },
            {
                "ColumnName": "avgmemutil",
                "Description": "Average memory utilization percentage during the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "avgcpuutil",
                "Description": "Average CPU utilization percentage during the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "avgswaputil",
                "Description": "Average swap/page file utilization percentage during the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "maxMemUtil",
                "Description": "Maximum memory utilization percentage observed in the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "maxCPUUtil",
                "Description": "Maximum CPU utilization percentage observed in the period",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "amportfolio_ril_idc_inv_biz_list",
                "Description": "Business list / business unit owning the asset in AM Portfolio",
                "DataType": "Text"
            },
            {
                "ColumnName": "ril_functional_group",
                "Description": "RIL functional/IT group responsible for supporting the asset",
                "DataType": "Text"
            },
            {
                "ColumnName": "location",
                "Description": "Physical rack/data center location of the server",
                "DataType": "Text"
            },
            {
                "ColumnName": "hostname",
                "Description": "Hostname from asset management",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_sitename",
                "Description": "Derived field - site name classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_environmentwise",
                "Description": "Derived field - environment classification (PRODUCTION, UAT, etc.)",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_location",
                "Description": "Derived field - location/site name classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_Top_Business_Line",
                "Description": "Derived field - top-level business line categorization",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_support_function",
                "Description": "Derived field - business support function name",
                "DataType": "Text"
            },
            {
                "ColumnName": "IPAddress",
                "Description": "Primary IP address of the server (In AM)",
                "DataType": "IP Address"
            },
            {
                "ColumnName": "d_ServerType",
                "Description": "Derived field - server type (Virtual Server / Physical Server)",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_oswise",
                "Description": "Derived field - OS family classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_statuswise",
                "Description": "Derived field - asset status classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "Related_IP",
                "Description": "Related or additional IP address(es) of the server",
                "DataType": "IP Address"
            },
            {
                "ColumnName": "ril_application_name",
                "Description": "Name of the primary application hosted on the server",
                "DataType": "Text"
            },
            {
                "ColumnName": "Username_App",
                "Description": "Application/support owner username (contact person)",
                "DataType": "Text"
            },
            {
                "ColumnName": "d_assetcateg",
                "Description": "Derived field - asset criticality category",
                "DataType": "Text"
            }
        ]
    },
    {
        "TableName": "BKP_Inventory",
        "Domain": "[BKP_Inventory].[dbo].[BKP_Inventory]",
        "Description": "Veritas Netbackup - enterprise-grade backup and recovery solution used by organizations to protect, manage, and recover data across complex IT environments.",
        "Columns": [
            {
                "ColumnName": "MasterServer",
                "Description": "Hostname of the NetBackup master server managing the backup policy",
                "DataType": "Text"
            },
            {
                "ColumnName": "PolicyName",
                "Description": "Unique name of the backup policy; encodes client, schedule day, time, and type",
                "DataType": "Text"
            },
            {
                "ColumnName": "PolicyType",
                "Description": "Type of backup policy engine used",
                "DataType": "Text"
            },
            {
                "ColumnName": "ActiveStatus",
                "Description": "Active status of the policy (1 = Active, 0 = Inactive)",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "IsIntelligentPolicy",
                "Description": "Flag indicating if this is an Intelligent Policy (1 = Yes, 0 = No)",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "FileSystem",
                "Description": "File systems or drives included in the backup scope",
                "DataType": "Text (List)"
            },
            {
                "ColumnName": "Client",
                "Description": "Hostname of the client server being backed up",
                "DataType": "Text"
            },
            {
                "ColumnName": "Retention",
                "Description": "Retention period(s) for each schedule type in the policy",
                "DataType": "Text (List)"
            },
            {
                "ColumnName": "Schedule",
                "Description": "List of schedule names corresponding to each backup type",
                "DataType": "Text (List)"
            },
            {
                "ColumnName": "BackupType",
                "Description": "Human-readable backup type labels for each schedule",
                "DataType": "Text (List)"
            },
            {
                "ColumnName": "Day",
                "Description": "Days of the week each schedule runs; outer list = schedule, inner list = days",
                "DataType": "Text (Nested List)"
            },
            {
                "ColumnName": "StartTime",
                "Description": "Start times for each schedule; outer list = schedule, inner list = times per day",
                "DataType": "Text (Nested List)"
            },
            {
                "ColumnName": "lPortfolioItemId",
                "Description": "Portfolio item identifier linking the client to the asset management system",
                "DataType": "Number"
            }
        ]
    },
    {
        "TableName": "BKP_Logs",
        "Domain": "[BKP_Logs].[dbo].[BKP_Logs]",
        "Description": "enterprise-grade backup and recovery solution used by organizations to protect, manage, and recover data across complex IT environments..Backup Inventory Log Information",
        "Columns": [
            {
                "ColumnName": "jobId",
                "Description": "Unique identifier for each backup/restore job execution",
                "DataType": "Number"
            },
            {
                "ColumnName": "MasterServer",
                "Description": "Hostname of the NetBackup master server managing the job",
                "DataType": "Text"
            },
            {
                "ColumnName": "parentJobId",
                "Description": "Job ID of the parent/root job; equals jobId for top-level jobs, 0 for standalone jobs",
                "DataType": "Number"
            },
            {
                "ColumnName": "activeProcessId",
                "Description": "Active Process Id",
                "DataType": "Number"
            },
            {
                "ColumnName": "mainProcessId",
                "Description": "Main Process Id",
                "DataType": "Number"
            },
            {
                "ColumnName": "jobType",
                "Description": "High-level type of job operation",
                "DataType": "Text"
            },
            {
                "ColumnName": "jobSubType",
                "Description": "Sub-type or trigger method of the job",
                "DataType": "Text"
            },
            {
                "ColumnName": "policyType",
                "Description": "NetBackup policy type governing the job",
                "DataType": "Text"
            },
            {
                "ColumnName": "policyName",
                "Description": "Name of the backup policy under which this job ran; empty for IMAGEDELETE jobs",
                "DataType": "Text (Reference key for Policy Inventory)"
            },
            {
                "ColumnName": "scheduleType",
                "Description": "Schedule type that triggered the job",
                "DataType": "Text"
            },
            {
                "ColumnName": "scheduleName",
                "Description": "Specific schedule name within the policy; '-' for parent-level jobs",
                "DataType": "Text"
            },
            {
                "ColumnName": "clientName",
                "Description": "Hostname of the client server/Asset being backed up",
                "DataType": "Text"
            },
            {
                "ColumnName": "controlHost",
                "Description": "Server Info",
                "DataType": "Text"
            },
            {
                "ColumnName": "jobOwner",
                "Description": "Job Owner",
                "DataType": "Text"
            },
            {
                "ColumnName": "jobGroup",
                "Description": "Job Group",
                "DataType": "Text"
            },
            {
                "ColumnName": "backupId",
                "Description": "Backup Identifier",
                "DataType": "Text"
            },
            {
                "ColumnName": "sourceMediaId",
                "Description": "Media ID of the source tape/disk",
                "DataType": "Text"
            },
            {
                "ColumnName": "sourceStorageUnitName",
                "Description": "Name of the source storage unit (for duplication jobs)",
                "DataType": "Text"
            },
            {
                "ColumnName": "sourceMediaServerName",
                "Description": "Media server hosting the source storage",
                "DataType": "Text"
            },
            {
                "ColumnName": "destinationMediaId",
                "Description": "Media ID of the destination (for copy/duplication jobs)",
                "DataType": "Text"
            },
            {
                "ColumnName": "destinationStorageUnitName",
                "Description": "Name of the destination storage unit where backup data is written",
                "DataType": "Text"
            },
            {
                "ColumnName": "destinationMediaServerName",
                "Description": "Hostname of the media server handling destination storage",
                "DataType": "Text"
            },
            {
                "ColumnName": "streamNumber",
                "Description": "streamNumber",
                "DataType": "Number"
            },
            {
                "ColumnName": "copyNumber",
                "Description": "copyNumber",
                "DataType": "Number"
            },
            {
                "ColumnName": "priority",
                "Description": "priority",
                "DataType": "Number"
            },
            {
                "ColumnName": "compression",
                "Description": "compression",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "status",
                "Description": "status",
                "DataType": "Number"
            },
            {
                "ColumnName": "state",
                "Description": "state",
                "DataType": "Text"
            },
            {
                "ColumnName": "done",
                "Description": "Completion flag (1 = completed, 0 = not completed)",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "numberOfFiles",
                "Description": "Actual number of files backed up in this job",
                "DataType": "Number"
            },
            {
                "ColumnName": "estimatedFiles",
                "Description": "estimatedFiles",
                "DataType": "Number"
            },
            {
                "ColumnName": "kilobytesTransferred",
                "Description": "Actual data transferred in kilobytes",
                "DataType": "Number (KB)"
            },
            {
                "ColumnName": "kilobytesToTransfer",
                "Description": "Estimated data to transfer in kilobytes; 0 in most records",
                "DataType": "Number (KB)"
            },
            {
                "ColumnName": "transferRate",
                "Description": "Data transfer rate in kilobytes per second",
                "DataType": "Number (KB/s)"
            },
            {
                "ColumnName": "percentComplete",
                "Description": "Job completion percentage (100 = fully complete)",
                "DataType": "Number (%)"
            },
            {
                "ColumnName": "restartable",
                "Description": "restartable",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "suspendable",
                "Description": "suspendable",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "resumable",
                "Description": "resumable",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "killable",
                "Description": "killable",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "frozenImage",
                "Description": "frozenImage",
                "DataType": "Number (Flag)"
            },
            {
                "ColumnName": "transportType",
                "Description": "transportType",
                "DataType": "Text"
            },
            {
                "ColumnName": "currentOperation",
                "Description": "currentOperation",
                "DataType": "Number/Text"
            },
            {
                "ColumnName": "robotName",
                "Description": "robotName",
                "DataType": "Text"
            },
            {
                "ColumnName": "vaultName",
                "Description": "vaultName",
                "DataType": "Text"
            },
            {
                "ColumnName": "profileName",
                "Description": "profileName",
                "DataType": "Text"
            },
            {
                "ColumnName": "sessionId",
                "Description": "sessionId",
                "DataType": "Number"
            },
            {
                "ColumnName": "numberOfTapeToEject",
                "Description": "numberOfTapeToEject",
                "DataType": "Number"
            },
            {
                "ColumnName": "submissionType",
                "Description": "submissionType",
                "DataType": "Number"
            },
            {
                "ColumnName": "dumpHost",
                "Description": "dumpHost",
                "DataType": "Text"
            },
            {
                "ColumnName": "instanceDatabaseName",
                "Description": "instanceDatabaseName",
                "DataType": "Text"
            },
            {
                "ColumnName": "auditUserName",
                "Description": "auditUserName",
                "DataType": "Text"
            },
            {
                "ColumnName": "auditDomainName",
                "Description": "auditDomainName",
                "DataType": "Text"
            },
            {
                "ColumnName": "auditDomainType",
                "Description": "auditDomainType",
                "DataType": "Number"
            },
            {
                "ColumnName": "restoreBackupIDs",
                "Description": "restoreBackupIDs",
                "DataType": "Text"
            },
            {
                "ColumnName": "startTime",
                "Description": "Actual start timestamp of the job",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "endTime",
                "Description": "Actual end timestamp of the job",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "activeTryStartTime",
                "Description": "activeTryStartTime",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "lastUpdateTime",
                "Description": "lastUpdateTime",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "initiatorId",
                "Description": "initiatorId",
                "DataType": "Text"
            },
            {
                "ColumnName": "retentionLevel",
                "Description": "retentionLevel",
                "DataType": "Number"
            },
            {
                "ColumnName": "try",
                "Description": "try",
                "DataType": "Number"
            },
            {
                "ColumnName": "jobQueueReason",
                "Description": "jobQueueReason",
                "DataType": "Number"
            },
            {
                "ColumnName": "jobQueueResource",
                "Description": "jobQueueResource",
                "DataType": "Text"
            },
            {
                "ColumnName": "kilobytesDataTransferred",
                "Description": "Actual user data transferred in kilobyte",
                "DataType": "Number (KB)"
            },
            {
                "ColumnName": "dataMovement",
                "Description": "Data movement mode (STANDARD = direct backup, no special movement)",
                "DataType": "Text"
            },
            {
                "ColumnName": "dedupRatio",
                "Description": "Deduplication ratio percentage; NULL if dedup not applicable",
                "DataType": "Decimal (%)"
            },
            {
                "ColumnName": "acceleratorOptimization",
                "Description": "Accelerator optimization percentage; 0 = no optimization, NULL if N/A",
                "DataType": "Number (%)"
            }
        ]
    },
    {
        "TableName": "SLA_ClosedTKT",
        "Domain": "[HPSM_Tickets].[dbo].[SLA_ClosedTKT]",
        "Description": "It\u2019s an IT Service Management (ITSM) ticketing tool used by IT teams to log, track, and manage service-related work across an organization.",
        "Columns": [
            {
                "ColumnName": "INCIDENT_ID",
                "Description": "Unique Service Desk ticket identifier (SD prefix)",
                "DataType": "Text"
            },
            {
                "ColumnName": "SD_OPEN_TIME",
                "Description": "Timestamp when the Service Desk ticket was created/logged",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "DEPEND",
                "Description": "Linked Incident/IM/RF number if this SD ticket was created from an escalation; NULL if standalone",
                "DataType": "Text"
            },
            {
                "ColumnName": "CONTACT_NAME",
                "Description": "Name of the user/entity who raised the ticket (person or RO store name)",
                "DataType": "Text"
            },
            {
                "ColumnName": "NUMBER",
                "Description": "Original IM (Incident Management) number if different from INCIDENT_ID; NULL for self-service",
                "DataType": "Text"
            },
            {
                "ColumnName": "OPEN_TIME",
                "Description": "Timestamp when the Service Desk ticket was created/logged",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "SEVERITY",
                "Description": "Ticket severity level (1=Critical, 2=High, 3=Medium, 4=Low), But we are not using this field for Priority .   There is a separate field names 'Priority' ",
                "DataType": "Number (1-4)"
            },
            {
                "ColumnName": "NETWORK_CONNECTVITY",
                "Description": "Type of network connection at user's location at time of issue; NULL if not applicable",
                "DataType": "Text"
            },
            {
                "ColumnName": "LOCATION",
                "Description": "Location/store code of the affected user or site; NULL for non-site tickets",
                "DataType": "Text"
            },
            {
                "ColumnName": "STORE_FORMAT_RIL",
                "Description": "Store format classification for Petro Retail outlets; NULL for non-retail tickets",
                "DataType": "Text"
            },
            {
                "ColumnName": "CATEGORY",
                "Description": "Top-level ticket type classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "OPEN",
                "Description": "Current open/closed status of the ticket",
                "DataType": "Text"
            },
            {
                "ColumnName": "CLOSED_BY",
                "Description": "User/system that closed the ticket",
                "DataType": "Text"
            },
            {
                "ColumnName": "COMPANY",
                "Description": "Company/entity owning the ticket; NULL for Enterprise IT tickets",
                "DataType": "Text"
            },
            {
                "ColumnName": "OPENED_BY",
                "Description": "Login ID or email through which the ticket was opened",
                "DataType": "Text"
            },
            {
                "ColumnName": "SUBCATEGORY",
                "Description": "Sub-classification of the ticket category (technical area)",
                "DataType": "Text"
            },
            {
                "ColumnName": "PRODUCT_TYPE",
                "Description": "Specific product/technology involved in the ticket",
                "DataType": "Text"
            },
            {
                "ColumnName": "PROBLEM_TYPE",
                "Description": "Nature/type of the specific problem reported",
                "DataType": "Text"
            },
            {
                "ColumnName": "TITLE",
                "Description": "Short title/summary of the ticket",
                "DataType": "Text"
            },
            {
                "ColumnName": "RSOL_BREACHENTITY",
                "Description": "Business entity against which SLA breach is tracked; NULL if not applicable",
                "DataType": "Text"
            },
            {
                "ColumnName": "DESCRIPTION",
                "Description": "Detailed description of the issue provided by the user or system",
                "DataType": "Text (Long)"
            },
            {
                "ColumnName": "RESOLUTION",
                "Description": "Resolution steps taken and outcome; NULL if auto-resolved without notes",
                "DataType": "Text (Long)"
            },
            {
                "ColumnName": "PRIORITY_CODE",
                "Description": "Priority code of the ticket (mirrors severity in most cases)",
                "DataType": "Number (1-4)"
            },
            {
                "ColumnName": "ASSIGNEE",
                "Description": "Login ID of the person/team the ticket was assigned to for resolution",
                "DataType": "Text"
            },
            {
                "ColumnName": "PROB_ASSIGNMENT",
                "Description": "Assignment group/queue where the ticket was routed",
                "DataType": "Text"
            },
            {
                "ColumnName": "ASSIGNEE_NAME",
                "Description": "Display name of the assignee (same as ASSIGNEE in most cases)",
                "DataType": "Text"
            },
            {
                "ColumnName": "IM_PRIORITY_CODE",
                "Description": "Priority code of the related Incident Management record",
                "DataType": "Number (1-4)"
            },
            {
                "ColumnName": "HANDLE_TIME",
                "Description": "Time taken to handle/resolve the ticket in DateTime format (4000-01-01 = base date offset)",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "CRITICAL_USER",
                "Description": "Flag indicating if the affected user is a critical/VIP user; NULL if unknown",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "RESOLUTION_CODE",
                "Description": "Standardized resolution outcome code",
                "DataType": "Text"
            },
            {
                "ColumnName": "CONTACT_EMAIL",
                "Description": "Email address of the contact/affected user",
                "DataType": "Email"
            },
            {
                "ColumnName": "RIL_CITY",
                "Description": "City of the affected user/site; NULL if not captured",
                "DataType": "Text"
            },
            {
                "ColumnName": "RIL_STATE",
                "Description": "State of the affected user/site; NULL if not captured",
                "DataType": "Text"
            },
            {
                "ColumnName": "DEPT",
                "Description": "Department of the affected user; NULL if not captured or auto-resolved",
                "DataType": "Text"
            },
            {
                "ColumnName": "REOPENCOUNT",
                "Description": "Number of times the ticket was reopened after initial closure; NULL for auto-resolved",
                "DataType": "Number"
            },
            {
                "ColumnName": "RIL_KM",
                "Description": "Knowledge Management article number used to resolve; NULL if no KM article applied",
                "DataType": "Number"
            },
            {
                "ColumnName": "APPROVAL_STATUS",
                "Description": "Approval workflow status for service catalog items; NULL for incidents/SR",
                "DataType": "Text"
            },
            {
                "ColumnName": "PROB_CATEGORY",
                "Description": "Category mapped in the Problem Management module; NULL if not linked",
                "DataType": "Text"
            },
            {
                "ColumnName": "PROB_SUBCATEGORY",
                "Description": "Subcategory in Problem Management; NULL if not linked",
                "DataType": "Text"
            },
            {
                "ColumnName": "IM_STATUS",
                "Description": "Status of the related Incident Management record",
                "DataType": "Text"
            },
            {
                "ColumnName": "RILRESOLVEDTIME",
                "Description": "Timestamp when the ticket was resolved/closed",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "IM_NETWORK_CONNECTVITY",
                "Description": "Network connectivity at time of IM resolution (may differ from original); NULL if unchanged",
                "DataType": "Text"
            },
            {
                "ColumnName": "BUSINESSENTITY",
                "Description": "Business entity/vertical the ticket belongs to",
                "DataType": "Text"
            },
            {
                "ColumnName": "VIP_USER",
                "Description": "VIP user flag; NULL if not classified",
                "DataType": "Text (t/f/NULL)"
            },
            {
                "ColumnName": "VVIP",
                "Description": "Very VIP user flag; NULL if not classified",
                "DataType": "Text (t/f/NULL)"
            },
            {
                "ColumnName": "RIL_KB",
                "Description": "Knowledge Base article reference; NA for self-service; NULL if not used",
                "DataType": "Text"
            },
            {
                "ColumnName": "SATISFY_OVERALL",
                "Description": "Customer satisfaction: overall rating; NULL if survey not completed",
                "DataType": "Number (1-5)"
            },
            {
                "ColumnName": "SATISFY_SPEED",
                "Description": "Customer satisfaction: speed of resolution rating",
                "DataType": "Number (1-5)"
            },
            {
                "ColumnName": "SATISFY_COMMUNICATION",
                "Description": "Customer satisfaction: communication quality rating",
                "DataType": "Number (1-5)"
            },
            {
                "ColumnName": "SATISFY_SKILLSET",
                "Description": "Customer satisfaction: agent skillset rating",
                "DataType": "Number (1-5)"
            },
            {
                "ColumnName": "SURVEYCOMMENTS",
                "Description": "Free text comments from customer satisfaction survey",
                "DataType": "Text"
            },
            {
                "ColumnName": "ESS_ENTRY",
                "Description": "Employee Self-Service entry flag; t = raised via self-service portal",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "ASSIGNMENT",
                "Description": "Final assignment group/team that resolved the ticket",
                "DataType": "Text"
            },
            {
                "ColumnName": "Log_mode",
                "Description": "Channel/mode through which the ticket was originally logged",
                "DataType": "Text"
            },
            {
                "ColumnName": "LOG_MODE_new",
                "Description": "Normalized/standardized log mode classification",
                "DataType": "Text"
            },
            {
                "ColumnName": "Req_NUMBER",
                "Description": "Request fulfillment number for service catalog items; NULL for incidents/SR",
                "DataType": "Text"
            },
            {
                "ColumnName": "Req_SLA_BREACH",
                "Description": "Flag indicating if the request SLA was breached; NULL if not applicable",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "Response_sla",
                "Description": "Flag indicating if the response SLA was met (f = met, t = breached)",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "Resolution_sla",
                "Description": "Flag indicating if the resolution SLA was met (f = met, t = breached)",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "d_Total_Time",
                "Description": "Derived Field - Total time taken to resolve the ticket. from open to close in human-readable format",
                "DataType": "Text (Duration)"
            },
            {
                "ColumnName": "Days_Diff",
                "Description": "Total calendar days from ticket open to close",
                "DataType": "Number"
            },
            {
                "ColumnName": "SBD",
                "Description": "Whether the ticket was resolved within SBD (Service Business Days); Yes = within SLA",
                "DataType": "Text (Yes/No)"
            },
            {
                "ColumnName": "additionalsoftwarerequired",
                "Description": "Flag indicating if additional software was required to resolve; NULL if not applicable",
                "DataType": "Text (t/f)"
            },
            {
                "ColumnName": "VENDOR",
                "Description": "Vendor involved in resolution (for hardware/dispenser issues); NULL if no vendor",
                "DataType": "Text"
            },
            {
                "ColumnName": "OVERALL_EXPERIANCE",
                "Description": "Free text or rating from overall experience feedback",
                "DataType": "Text"
            }
        ]
    },
    {
        "TableName": "CR_Asset",
        "Domain": "[HPSM_Tickets].[dbo].[CR_Asset]",
        "Description": "Change Management tickets which contains CI names",
        "Columns": [
            {
                "ColumnName": "cm2rm1_NUMBER",
                "Description": "Unique Change Management ticket identifier (C prefix)",
                "DataType": "Text"
            },
            {
                "ColumnName": "CATEGORY",
                "Description": "Type/category of the change request",
                "DataType": "Text"
            },
            {
                "ColumnName": "REQSTARTDATE",
                "Description": "Requested start date and time for the change window/maintenance activity",
                "DataType": "DateTime"
            },
            {
                "ColumnName": "cmra3_NUMBER",
                "Description": "same as row no. 1",
                "DataType": "Text"
            },
            {
                "ColumnName": "RECORD_NUMBER",
                "Description": NaN,
                "DataType": "Number"
            },
            {
                "ColumnName": "ASSETS",
                "Description": "Configuration Item (CI) identifier from the CMDB linked to the change",
                "DataType": "Text"
            },
            {
                "ColumnName": "DISPLAY_NAME",
                "Description": "Hostname of the CI asset being changed",
                "DataType": "Text"
            }
        ]
    }
]

# # Define your global database model
# global_database_model = {
#     "tables": table_descriptions,
#     "rules": json_rules
# }

