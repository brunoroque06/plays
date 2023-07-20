$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'
$loc = 'West Europe'
$rg = 'rg-dug'

az group delete --subscription $sub --name $rg --yes
az deployment sub create --sub $sub --location $loc --template-file main.bicep --parameters location=$loc resourceGroupName=$rg
