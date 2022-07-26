terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.13.0"
    }
  }
}

provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "shamithash1" {
  name         = "shamithash1:latest"
  keep_locally = false
  build {
    path = "."
    tag  = ["shamithash1:latest"]
  }
}

