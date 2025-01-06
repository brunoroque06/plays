terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "st4tfstate"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.14.0"
    }
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "azurerm" {
  tenant_id       = "802458a5-5f60-41a0-b729-c79de49878a2"
  subscription_id = "ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8"
  features {}
}

provider "docker" {
  host = "unix://${pathexpand("~/.docker/run/docker.sock")}"
}

variable "az_loc" {
  type    = string
  default = "westeurope"
}
