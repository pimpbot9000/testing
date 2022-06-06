variable "meat" {
    type = string
    default = "chicken"
}

module "my_salsa" {
    source ="./salsa"
    meat = var.meat
}

locals {
    taco = {
        meat = var.meat
        cheese = "jack"
        shell = "crunchy"
        salsa = module.my_salsa.salsa
    }
}

output "taco" {
  value = local.taco
}