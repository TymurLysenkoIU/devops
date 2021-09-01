# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.74.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  # Set valid values
  subscription_id   = "<azure_subscription_id>"
  tenant_id         = "<azure_subscription_tenant_id>"
  client_id         = "<service_principal_appid>"
  client_secret     = "<service_principal_password>"
}

# Create a resource group
resource "azurerm_resource_group" "iu-devops" {
  name     = "iu-devops-group"
  location = "West Europe"
}

# Run the container
resource "azurerm_container_group" "tymur-lysenko-iu-devoups" {
  name                = "tymur-lysenko-iu-devoups"
  location            = azurerm_resource_group.iu-devops.location
  resource_group_name = azurerm_resource_group.iu-devops.name
  ip_address_type     = "public"
  os_type             = "linux"

  container {
    name   = "python-app"
    image  = "sitiritis/iu-devops:latest"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port = 80
    }
  }
}
