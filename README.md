# Terraform Cloud Platform Project

An end-to-end Terraform project for provisioning a small AWS static website platform.

## What this project demonstrates

- Terraform provider configuration and reusable variables
- S3 bucket configuration for website hosting
- CloudFront distribution for HTTPS delivery
- Origin Access Control so the bucket is not public
- DynamoDB-backed state locking configuration notes
- Terraform formatting, validation, and plan checks in GitHub Actions

## Local validation

```powershell
terraform init
terraform fmt -check
terraform validate
terraform plan -var="project_name=devyansh-terraform-demo" -var="environment=dev"
```

The plan requires AWS credentials because the AWS provider reads account metadata. No `terraform apply` is performed automatically.

## Deployment

1. Configure AWS credentials locally or as GitHub Actions secrets.
2. Review `terraform.tfvars.example` and create `terraform.tfvars`.
3. Run `terraform plan` and review the output.
4. Run `terraform apply` only after confirming the resource changes.

## Author

Devyansh Gupta (USN: 25MCAR0193)
