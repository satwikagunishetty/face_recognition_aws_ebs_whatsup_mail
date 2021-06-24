resource "aws_instance" "web" {
    ami="ami-0ad704c126371a549"
    instance_type = var.type["ap-south-1"]
    //count=var.test?0:1
    key_name = "terra"
    
    //count=1
  connection {
     type = "ssh"
     user = "ec2-user"
     private_key = file("C:/Users/hp/Desktop/terra.pemm")
     host = aws_instance.web.public_ip
}

  
}
resource "aws_ebs_volume" "ebs_v1" {
  availability_zone = aws_instance.web.availability_zone
  size              = 5

  tags = {
    Name = "5GB_Ebs_Volume"
  }
}
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.ebs_v1.id
  instance_id = aws_instance.web.id
   force_detach = true
}
