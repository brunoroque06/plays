targetScope = 'resourceGroup'

param location string

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
  location: location
  properties: {
    serverFarmId: plan.id
    siteConfig: {
      appCommandLine: 'python -m streamlit run Home.py --server.address 0.0.0.0 --server.port 8000'
      linuxFxVersion: 'Python|3.11'
    }
  }
}

resource code 'Microsoft.Web/sites/sourcecontrols@2022-09-01' = {
  parent: app
  name: 'web'
  properties: {
    repoUrl: 'https://github.com/brunoroque06/plays'
    branch: 'st'
    isManualIntegration: true
  }
}
