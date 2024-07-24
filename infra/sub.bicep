targetScope = 'subscription'

@allowed(['westeurope'])
param location string

resource rgPer 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  location: location
  name: 'rg-personal'
}

module personal 'personal.bicep' = {
  name: 'personal'
  scope: rgPer
  params: {
    location: rgPer.location
  }
}

resource rgRep 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  location: location
  name: 'rg-reportus'
}

module reportus 'reportus.bicep' = {
  name: 'reportus'
  scope: rgRep
  params: {
    location: rgRep.location
  }
}
