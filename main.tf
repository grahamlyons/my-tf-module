resource "random_id" "id" {
  byte_length = 8
}

resource "random_pet" "name" {
    length = 2
    separator = "_"
}

output "id" {
    value = "${random_id.id.hex}"
}

output "name" {
    value = "${random_pet.name.id}"
}
