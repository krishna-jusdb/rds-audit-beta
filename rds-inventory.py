"""Script to export RDS list into .csv"""

import boto3
import pandas as pd

client = boto3.client('rds')

response = client.describe_db_instances()

db_name = []
db_engine = []
db_version = []
db_status = []
db_class = []
db_multiaz = []
db_security_groups = []
db_vpc = []
db_vpc_security_groups = []
db_subnets = []
db_backup = []
db_storage = []
db_auto_upgrade = []
db_del_protection = [] 
db_storage_type = []
db_iops = []
db_storage_max = []
db_storage_encrypted = []


for x in response['DBInstances']:
    db_name.append(x['DBInstanceIdentifier'])
    db_class.append(x['DBInstanceClass'])
    db_engine.append(x['Engine'])
    db_version.append(x['EngineVersion'])
    db_status.append(x['DBInstanceStatus'])
    db_storage.append(x['AllocatedStorage'])
    db_backup.append(x['BackupRetentionPeriod'])
    db_auto_upgrade.append(x['AutoMinorVersionUpgrade'])
    db_del_protection.append(x['DeletionProtection'])
    db_storage_type.append(x['StorageType'])
    db_iops.append(x.get('Iops','NA')) 
    db_storage_max.append(x.get('MaxAllocatedStorage','NA'))
    db_storage_encrypted.append(x['StorageEncrypted'])
    if x['MultiAZ'] is True:
        db_multiaz.append('Yes')
    else:
        db_multiaz.append('no')
    

db_info = {"name":db_name, "engine": db_engine,"db_version":db_version,"status": db_status,"instance type": db_class,"Size GiB": db_storage, "multiAZ":db_multiaz, "db_backup_retention":db_backup, "db_storage_type":db_storage_type,"db_storage":db_storage,"db_storage_max":db_storage_max,"db_storage_encrypted":db_storage_encrypted,"db_del_protection":db_del_protection,"db_auto_upgrade":db_auto_upgrade,"db_iops":db_iops }

df_rds = pd.DataFrame(db_info)

print(df_rds)

# Change the string below to change the name of the output file
df_rds.to_csv('rds-inventory.csv')
