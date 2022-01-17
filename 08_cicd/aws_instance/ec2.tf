provider "aws" {
  region = "us-east-2"
}

output "public_dns" {
  value = aws_instance.jenkins[*].public_dns
}

resource "local_file" "terraform_ssh_key" {
    content     = tls_private_key.ansible_key.private_key_pem
    filename = "/home/bvaradinov/.ssh/id_rsa_terraform"
    file_permission = "0600"
}
resource "tls_private_key" "ansible_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "ansible_user" {
  key_name   = "ansible_user_jenkins"
  public_key = tls_private_key.ansible_key.public_key_openssh
}

resource "aws_instance" "jenkins" {
  count = 1 
  
  ami           = "ami-0a0ad6b70e61be944"
  instance_type = "t2.micro"
  security_groups = [ aws_security_group.allow_web_traffic.name ]
  key_name = aws_key_pair.ansible_user.key_name


  tags = {
    Name = "jenkins_${count.index}"
    Role = "jenkins"
  }
}


resource "aws_security_group" "allow_web_traffic" {
  name        = "allow_jenkins_traffic"
  description = "Allow inbound jenkins traffic"

  ingress {
    description = "TLS from VPC"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "TLS from VPC"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  
  ingress {
    description = "TLS from VPC"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "TLS from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_jenkins_traffic"
  }
}