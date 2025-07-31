# Cost monitoring script
Get-AzConsumptionUsageDetail \
  -StartDate (Get-Date).AddDays(-30).ToString("yyyy-MM-dd") \
  -EndDate (Get-Date).ToString("yyyy-MM-dd") \
  | Where-Object {$_.ResourceType -like "Microsoft.DocumentDB/*"} \
  | Select-Object InstanceName, PreTaxCost, MeterCategory, UsageStart, UsageEnd \
  | Format-Table -AutoSize
