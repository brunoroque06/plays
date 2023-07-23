$loc = 'West Europe'
$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'

az deployment sub create `
  --location $loc `
  --parameters location=$loc `
  --sub $sub `
  --template-file main.bicep

docker build --platform linux/amd64 --tag crdug.azurecr.io/dug ..
az acr login --name crdug
docker push crdug.azurecr.io/dug
az webapp restart --name app-dug --resource-group rg-dug