$ErrorActionPreference = "Stop"

$loc = 'West Europe'
$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'

Connect-AzAccount -Subscription $sub
Set-AzContext -Subscription $sub

New-AzDeployment `
  -Location $loc `
  -TemplateFile subscription.bicep `
  -TemplateParameterObject @{ location = $loc }

Push-Location ../reportus

docker build --platform linux/amd64 --tag crmaino.azurecr.io/reportus ..
Connect-AzContainerRegistry maino
docker push crmaino.azurecr.io/reportus
Restart-AzWebApp -Name app-reportus -ResourceGroupName rg-main
