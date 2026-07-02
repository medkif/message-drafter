output "project_id" {
  value = var.project_id
}
output "project_number" {
  value = var.project_number
}
output "region" {
  value = var.region
}
output "id_deployer_sa" {
  value = var.id_github_sa
}
output "deployer_email" {
  value = module.deployer_sa.service_account_email
}
output "runner_email" {
  value = module.runtime_sa.service_account_email
}
output "repository_id" {
  value = var.repository_id
}
output "workload_identity_pool_name" {
  value = module.workload_identity.workload_identity_pool_name
}

output "github_owner" {
  value = var.github_owner
}
output "github_repo" {
  value = var.github_repo
}
