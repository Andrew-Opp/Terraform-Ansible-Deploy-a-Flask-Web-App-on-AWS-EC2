output "web_instance_ips" {
  description = "Public IPs of EC2 web servers"
  value       = [aws_instance.instance_1.public_ip, aws_instance.instance_2.public_ip]
}

output "alb_dns_name" {
  description = "ALB DNS name"
  value       = aws_lb.load_balancer.dns_name
}

output "private_key_path" {
  description = "Path to SSH private key"
  value       = local_file.private_key.filename
}
