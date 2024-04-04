targetScope = 'subscription'

@allowed(['westeurope'])
param location string

resource rg 'Microsoft.Resources/resourceGroups@2023-07-01' = {
  location: location
  name: 'rg-main'
}

module reportus 'rg.bicep' = {
  name: 'apps'
  scope: rg
  params: {
    location: rg.location
  }
}
