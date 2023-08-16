$loc = 'West Europe'
$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'

az deployment sub create `
  --location $loc `
  --parameters location=$loc `
  --sub $sub `
  --template-file main.bicep

docker build --platform linux/amd64 --tag crreportus.azurecr.io/reportus ..
az acr login --name crreportus
docker push crreportus.azurecr.io/reportus
az webapp restart --name app-reportus --resource-group rg-reportus