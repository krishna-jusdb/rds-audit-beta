import boto3
client = boto3.client('ce')
import pandas as pd

response = client.get_reservation_purchase_recommendation(
    Service='Amazon Relational Database Service',
    LookbackPeriodInDays='THIRTY_DAYS',
    TermInYears='ONE_YEAR',
    PaymentOption='NO_UPFRONT',
    PageSize=123,
)

AccountId = []
AverageUtilization = []
CurrencyCode = []
EstimatedMonthlyOnDemandCost = []
EstimatedMonthlySavingsAmount = []
EstimatedMonthlySavingsPercentage = []
EstimatedMonthlySavingsPercentage = []
DatabaseEngine = []
InstanceType = []
InstanceRegion = []
ToPurchase = []

for suggestions in response['Recommendations']:
    for details in suggestions['RecommendationDetails']:
        AccountId.append(details['AccountId'])
        AverageUtilization.append(details['AverageUtilization'])
        CurrencyCode.append(details['CurrencyCode'])
        EstimatedMonthlyOnDemandCost.append(details['EstimatedMonthlyOnDemandCost'])
        EstimatedMonthlySavingsAmount.append(details['EstimatedMonthlySavingsAmount'])
        EstimatedMonthlySavingsPercentage.append(details['EstimatedMonthlySavingsPercentage'])
        DatabaseEngine.append(details['InstanceDetails']['RDSInstanceDetails']['DatabaseEngine'])
        InstanceType.append(details['InstanceDetails']['RDSInstanceDetails']['InstanceType'])
        InstanceRegion.append(details['InstanceDetails']['RDSInstanceDetails']['Region'])
        ToPurchase.append(details['RecommendedNumberOfInstancesToPurchase'])


ri_info = {"AccountId":AccountId,
"AverageUtilization":AverageUtilization,
"CurrencyCode":CurrencyCode,
"InstanceRegion":InstanceRegion,
"InstanceType":InstanceType,
"DatabaseEngine":DatabaseEngine, 
"ToPurchase":ToPurchase,
"EstimatedMonthlyOnDemandCost":EstimatedMonthlyOnDemandCost,
"EstimatedMonthlySavingsAmount":EstimatedMonthlySavingsAmount,
"EstimatedMonthlySavingsPercentage":EstimatedMonthlySavingsPercentage,
}

df_ri = pd.DataFrame(ri_info)

print(df_ri)

# # Change the string below to change the name of the output file
df_ri.to_csv('ri-recommendations.csv')