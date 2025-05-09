# Security Group for EC2 instances
resource "aws_security_group" "app_sg" {
  name        = "bookstore-app-sg"
  description = "Security group for bookstore application"
  vpc_id      = module.vpc.vpc_id

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
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
    Name = "bookstore-app-sg"
  }
}

# EC2 Instance
resource "aws_instance" "app_server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = module.vpc.public_subnets[0]
  key_name      = var.key_name

  vpc_security_group_ids = [aws_security_group.app_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              usermod -a -G docker ec2-user
              curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              
              # Create data directory for SQLite
              mkdir -p /home/ec2-user/data
              chmod 777 /home/ec2-user/data
              EOF

  tags = {
    Name = "bookstore-app-server"
  }
}

# Elastic IP for the EC2 instance
resource "aws_eip" "app_eip" {
  instance = aws_instance.app_server.id
  domain   = "vpc"
  tags = {
    Name = "bookstore-app-eip"
  }
}