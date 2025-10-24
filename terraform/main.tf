# terraform/main.tf

terraform {
  required_version = ">= 1.0.0"
}

provider "local" {}

resource "local_file" "infraestructura" {
  filename = "${path.module}/infraestructura.txt"
  content  = <<EOT
Infraestructura simulada creada con Terraform
----------------------------------------------
Este archivo representa el entorno preparado para el análisis de pacientes.
EOT
}

output "mensaje" {
  value = "✅ Infraestructura simulada creada correctamente."
}
