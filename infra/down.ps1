$ErrorActionPreference = "Stop"

$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'

Connect-AzAccount -Subscription $sub
Set-AzContext -Subscription $sub

Remove-AzResourceGroup rg-main
