resource "azurerm_resource_group" "tfstate" {
  name     = "rg-tfstate"
  location = var.az_loc
}

resource "azurerm_storage_account" "tfstate" {
  account_replication_type          = "ZRS"
  account_tier                      = "Standard"
  infrastructure_encryption_enabled = true
  location                          = azurerm_resource_group.tfstate.location
  name                              = "st4tfstate"
  resource_group_name               = azurerm_resource_group.tfstate.name
}

resource "azurerm_storage_container" "tfstate" {
  name               = "tfstate"
  storage_account_id = azurerm_storage_account.tfstate.id
}
