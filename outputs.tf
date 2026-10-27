output "cloudtrail_arn" {
  description = "ARN of the CloudTrail trail."
  value       = aws_cloudtrail.main.arn
}

output "cloudtrail_name" {
  description = "Name of the CloudTrail trail."
  value       = aws_cloudtrail.main.name
}

output "s3_bucket_name" {
  description = "Name of the shared S3 bucket for logs."
  value       = aws_s3_bucket.logs.id
}

output "s3_bucket_arn" {
  description = "ARN of the shared S3 bucket for logs."
  value       = aws_s3_bucket.logs.arn
}

output "cloudtrail_s3_prefix" {
  description = "S3 prefix used by CloudTrail."
  value       = var.cloudtrail_s3_prefix
}

output "vpc_flow_logs_s3_prefix" {
  description = "S3 prefix reserved for VPC Flow logs."
  value       = var.vpc_flow_logs_s3_prefix
}
