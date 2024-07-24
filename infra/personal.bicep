targetScope = 'resourceGroup'

@allowed(['westeurope'])
param location string

resource website 'Microsoft.Web/staticSites@2023-12-01' = {
  location: location
  name: 'stapp-personal'
  properties: {}
  sku: {
    name: 'Free'
  }
}
