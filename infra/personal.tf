resource "azurerm_resource_group" "per" {
  name     = "rg-personal"
  location = var.az_loc
}

resource "azurerm_static_web_app" "per" {
  resource_group_name = azurerm_resource_group.per.name
  location            = azurerm_resource_group.per.location
  name                = "stapp-personal"
  sku_size            = "Free"
}

resource "azurerm_static_web_app_custom_domain" "per" {
  static_web_app_id = azurerm_static_web_app.per.id
  domain_name       = "broque.dev"
  validation_type   = "dns-txt-token" // Apex Domains must use "dns-txt-token" validation
}
