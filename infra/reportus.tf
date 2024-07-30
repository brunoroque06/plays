resource "docker_image" "rep" {
  name = "brunoroque06/reportus"
  build {
    context = "../reportus"
    platform = "linux/amd64"
  }
  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "../reportus/*") : filesha1(f)]))
  }
}

# resource "docker_registry_image" "rep" {
#   name          = docker_image.rep.name
#   keep_remotely = true
# }

resource "azurerm_resource_group" "rep" {
  name     = "rg-reportus"
  location = var.az_loc
}

resource "azurerm_service_plan" "rep" {
  name                = "plan-linux"
  resource_group_name = azurerm_resource_group.rep.name
  location            = azurerm_resource_group.rep.location
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "rep" {
  name                = "app-reportus"
  resource_group_name = azurerm_resource_group.rep.name
  location            = azurerm_service_plan.rep.location
  service_plan_id     = azurerm_service_plan.rep.id
  app_settings = {
    WEBSITES_PORT = "8080"
  }
  site_config {
    always_on = false
    application_stack {
      docker_image_name = "brunoroque06/reportus"
    }
  }
}
