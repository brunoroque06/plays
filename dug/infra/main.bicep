targetScope = 'subscription'

param location string
param resourceGroupName string

resource rg 'Microsoft.Resources/resourceGroups@2022-09-01' = {
  location: location
  name: resourceGroupName
}

module app 'app.bicep' = {
  name: 'appDeployment'
  scope: rg
  params: {
    location: rg.location
  }
}
