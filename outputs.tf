output "website_bucket_name" {
  description = "Private S3 bucket containing website assets."
  value       = aws_s3_bucket.website.bucket
}

output "cloudfront_distribution_id" {
  description = "CloudFront distribution identifier."
  value       = aws_cloudfront_distribution.website.id
}

output "cloudfront_domain_name" {
  description = "HTTPS domain name for the deployed website."
  value       = aws_cloudfront_distribution.website.domain_name
}
