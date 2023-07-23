targetScope = 'resourceGroup'

param location string

resource cr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  location: location
  name: 'crdug'
  properties: {
    adminUserEnabled: true
  }
  sku: {
    name: 'Basic'
  }
}

var user = '8e5b7c2a-3149-45e7-a7ee-3424704f6e75' // https://github.com/Azure/bicep/issues/645

resource acrPull 'Microsoft.Authorization/roleDefinitions@2022-05-01-preview' existing = {
  name: '7f951dda-4ed3-4680-a7ca-43fe172d538d' // AcrPull
  scope: subscription()
}

resource acrPush 'Microsoft.Authorization/roleDefinitions@2022-05-01-preview' existing = {
  name: '8311e382-0749-4cb8-b61a-304f252e45ec' // AcrPush
  scope: subscription()
}

resource crUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(cr.id, user)
  properties: {
    principalId: user
    roleDefinitionId: acrPush.id
  }
  scope: cr
}

resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  location: location
  name: 'plan-linux-free'
  kind: 'linux'
  properties: {
    reserved: true
  }
  sku: {
    name: 'F1'
  }
}

resource app 'Microsoft.Web/sites@2022-09-01' = {
  name: 'app-dug'
  identity: {
    type: 'SystemAssigned'
  }
  location: location
  properties: {
    serverFarmId: plan.id
    siteConfig: {
      acrUseManagedIdentityCreds: true
      linuxFxVersion: 'DOCKER|${cr.name}.azurecr.io/dug:latest'
    }
  }
}

resource crApp 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(cr.id, app.id)
  properties: {
    principalId: app.identity.principalId
    roleDefinitionId: acrPull.id
  }
  scope: cr
}
