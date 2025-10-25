output "project_id" {
  value = var.project_id
}
output "project_number" {
  value = var.project_number
}
output "region" {
  value = var.region
}
output "service_account_id" {
  value = var.service_account_id
}
output "service_account_email" {
  value = module.service_account.service_account_email
}
output "repository_id" {
  value = var.repository_id
}
output "workload_identity_pool_id" {
  value = var.workload_identity_pool_id
}
output "github_owner" {
  value = var.github_owner
}
output "github_repo" {
  value = var.github_repo
}
