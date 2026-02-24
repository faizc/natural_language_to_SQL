table_descriptions = [
    {
        "TableName": "AM",
        "Description": "Asset Management",
        "Domain": "[AMDATA].[dbo].[con_am_asset_lifecycle]"
    },
    {
        "TableName": "Monitoring",
        "Description": "Monitoring",
        "Domain": "Monitoring"
    },
    {
        "TableName": "BKP_Inventory",
        "Description": "Backup Inventory Information",
        "Domain": "BKP_Inventory"
    },
    {
        "TableName": "BKP_Logs",
        "Description": "Backup Inventory Log Information",
        "Domain": "BKP_Logs"
    }
]


json_rules = """
  "rules": [
  ]
"""


global_database_model = [
    {
        "TableName": "AM",
        "Description": "Asset Management",
        "Domain": "[AMDATA].[dbo].[con_am_asset_lifecycle]",
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
        "Description": "Monitoring",
        "Domain": "Monitoring",
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
        "Description": "Backup Inventory Information",
        "Domain": "BKP_Inventory",
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
        "Description": "Backup Inventory Log Information",
        "Domain": "BKP_Logs",
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
    }
]

# # Define your global database model
# global_database_model = {
#     "tables": table_descriptions,
#     "rules": json_rules
# }

