variable "x" {
 default=false
    type=bool 
}
variable "z" {
default=false
    type=bool
}
variable "test" {
    default=false
    type=bool
}
variable "type" {
    type = map
    default = {
     ap-south-1= "t2.micro"
    }

}
variable "azs" {
  default = ["ap-south-1a"]
}


output "y" {
    value = var.test?"vim":"jtfyt"
  
}
output "h" {
    value = var.z
  
}
variable "vpc_cidr" {
default = "10.0.0.0/16"
  
}

variable "subnets_cidr" {
type = list
default = ["10.0.1.0/24","10.0.2.0/24"]
  
}