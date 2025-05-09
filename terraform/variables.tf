variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0c7217cdde317cfec"  # Amazon Linux 2023 AMI
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of the SSH key pair to use for the EC2 instance"
  type        = string
  default     = "bookstore-key"
}