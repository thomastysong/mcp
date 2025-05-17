# Query Intune for non-compliant devices using Microsoft Graph
param()

Install-Module Microsoft.Graph.Intune -Force -Scope CurrentUser
Connect-MSGraph -AccessToken $env:GRAPH_TOKEN
$devices = Get-IntuneManagedDevice | Where-Object { $_.ComplianceState -eq 'noncompliant' }
$devices | Export-Csv -Path intune_noncompliant.csv -NoTypeInformation
