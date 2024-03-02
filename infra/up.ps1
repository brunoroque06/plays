$ErrorActionPreference = "Stop"

$loc = 'West Europe'
$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'
$ten = '802458a5-5f60-41a0-b729-c79de49878a2'

az login --tenant $ten

az deployment sub create `
  --location $loc `
  --parameters location=$loc `
  --sub $sub `
  --template-file subscription.bicep

Push-Location ../reportus

docker build --platform linux/amd64 --tag crmaino.azurecr.io/reportus .
az acr login --name crmaino
docker push crmaino.azurecr.io/reportus
az webapp restart --name app-reportus --resource-group rg-main
