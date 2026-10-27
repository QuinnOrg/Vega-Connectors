variable "aws_region" {
  description = "AWS region for CloudTrail and the shared log bucket."
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the shared S3 bucket for CloudTrail and VPC Flow logs. Must be globally unique."
  type        = string
}

variable "trail_name" {
  description = "Name of the CloudTrail trail."
  type        = string
  default     = "account-cloudtrail-us-east-1"
}

variable "cloudtrail_s3_prefix" {
  description = "S3 key prefix for CloudTrail log files."
  type        = string
  default     = "cloudtrail"
}

variable "vpc_flow_logs_s3_prefix" {
  description = "S3 key prefix reserved for VPC Flow logs (used in bucket policy; provisioned by the vpc-flow-logs template)."
  type        = string
  default     = "vpc-flow-logs"
}

variable "enable_log_file_validation" {
  description = "Enable CloudTrail log file integrity validation."
  type        = bool
  default     = true
}

variable "enable_bucket_versioning" {
  description = "Enable S3 bucket versioning for the shared log bucket."
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags applied to created resources."
  type        = map(string)
  default     = {}
}
