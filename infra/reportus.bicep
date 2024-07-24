targetScope = 'resourceGroup'

@allowed(['westeurope'])
param location string

resource plan 'Microsoft.Web/serverfarms@2023-12-01' = {
  location: location
  name: 'plan-linux'
  kind: 'linux'
  properties: {
    reserved: true
  }
  sku: {
    name: 'F1'
  }
}

resource app 'Microsoft.Web/sites@2023-12-01' = {
  name: 'app-reportus'
  identity: {
    type: 'SystemAssigned'
  }
  location: location
  properties: {
    serverFarmId: plan.id
    siteConfig: {
      acrUseManagedIdentityCreds: true
      appSettings: [
        {
          name: 'WEBSITES_PORT'
          value: '8080'
        }
      ]
      linuxFxVersion: 'DOCKER|brunoroque06/reportus'
    }
  }
}
