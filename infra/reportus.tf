resource "docker_image" "rep" {
  name = "brunoroque06/reportus"
  build {
    context  = "../reportus"
    platform = "linux/amd64"
  }
  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "../reportus/*") : filesha1(f)]))
  }
}

resource "terraform_data" "rep_push" {
  provisioner "local-exec" {
    command = "docker push ${docker_image.rep.name}"
  }
  triggers_replace = {
    image_id = docker_image.rep.image_id
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

resource "azurerm_log_analytics_workspace" "rep" {
  name                = "log-reportus"
  location            = azurerm_resource_group.rep.location
  resource_group_name = azurerm_resource_group.rep.name
  sku                 = "PerGB2018"
}

resource "azurerm_container_app_environment" "rep" {
  name                       = "cae-reportus"
  location                   = azurerm_resource_group.rep.location
  resource_group_name        = azurerm_resource_group.rep.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.rep.id

}

resource "azurerm_container_app" "rep" {
  name                         = "ca-reportus"
  container_app_environment_id = azurerm_container_app_environment.rep.id
  resource_group_name          = azurerm_resource_group.rep.name
  ingress {
    allow_insecure_connections = false
    external_enabled           = true
    target_port                = 8080
    traffic_weight {
      latest_revision = true
      percentage      = 100
    }
  }
  revision_mode = "Single"
  template {
    container {
      name   = "reportus"
      image  = "registry-1.docker.io/${docker_image.rep.name}:latest"
      cpu    = 0.25
      memory = "0.5Gi"
    }
    max_replicas = 1
    min_replicas = 0
  }
}

# https://github.com/hashicorp/terraform-provider-azurerm/issues/21866
resource "terraform_data" "rep_add_domain" {
  provisioner "local-exec" {
    command    = "az containerapp hostname add --ids ${azurerm_container_app.rep.id} --hostname reportus.app"
    on_failure = continue
  }
  provisioner "local-exec" {
    command = "az containerapp hostname bind --ids ${azurerm_container_app.rep.id} --hostname reportus.app -e ${azurerm_container_app_environment.rep.name} --validation-method TXT"
  }
  lifecycle {
    replace_triggered_by = [azurerm_container_app.rep]
  }
}
