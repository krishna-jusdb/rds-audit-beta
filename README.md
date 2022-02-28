# rds-audit-beta
collect metadata of the rds instance infra before audit


Requirements:
> Python3.6
pandas
boto3

Either use aws access/secret keys or execute from the ec2 with below roles

```
service: RDS

{
    "Version": "2012-10-17",
    "Statement": [

        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "rds:DescribeDBInstances",
            ],
            "Resource": "*"
        }
    ]
}

service: Cost Explorer
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ce:GetReservationUtilization",
                "ce:GetReservationCoverage",
                "ce:GetReservationPurchaseRecommendation"
            ],
            "Resource": "*"
        }
    ]
}
```
Run : 
python3 rds-inventory.py 

python3 cost-explorer.py

Outputs: 
rds-inventory.csv
ri-recommendations.csv
