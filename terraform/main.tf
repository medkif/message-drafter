# Pre-requisite: Project needs to exist
provider "google" {
  project = var.project_id
  region  = var.region
}

# Module for activating APIs in GCP
module "apis" {
  source = "../infra/gcp-iac/modules/apis"
  required_apis = var.required_apis
  project_id    = var.project_id
}

module "service_account" {
  source             = "../infra/gcp-iac/modules/service_account"
  project_id         = var.project_id
  service_account_id = var.service_account_id
  user_email         = var.user_email
  sa_roles           = var.sa_roles
}

module "workload_identity" {
  source                    = "../infra/gcp-iac/modules/workload_identity"
  project_id                = var.project_id
  project_number            = var.project_number
  workload_identity_pool_id = var.workload_identity_pool_id
  github_owner              = var.github_owner
  github_repo               = var.github_repo
  service_account_email     = module.service_account.service_account_email
  depends_on = [ module.service_account, module.apis]
}

module "artifact_registry" {
  source        = "../infra/gcp-iac/modules/artifact_registry"
  repository_id = var.repository_id
  region        = var.region
  depends_on = [ module.apis ]
}