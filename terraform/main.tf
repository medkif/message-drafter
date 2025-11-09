# Pre-requisite: Project needs to exist
provider "google" {
  project = var.project_id
  region  = var.region
}

# Module for activating APIs in GCP
module "apis" {
  source = "../../infra/gcp-iac/modules/apis"
  required_apis = var.required_apis
  project_id    = var.project_id
}

# Deployer SA
module "deployer_sa" {
  source             = "../../infra/gcp-iac/modules/service_account"
  project_id         = var.project_id
  service_account_id = var.id_github_sa
  user_email         = var.user_email
  depends_on = [ module.apis ]
}

# Runtime SA
module "runtime_sa" {
  source             = "../../infra/gcp-iac/modules/service_account"
  project_id         = var.project_id
  service_account_id = var.id_runtime_sa
  user_email         = var.user_email
  sa_roles           = var.sa_roles
  depends_on = [ module.apis ]
}

module "workload_identity" {
  source                    = "../../infra/gcp-iac/modules/workload_identity"
  project_id                = var.project_id
  project_number            = var.project_number
  workload_identity_pool_id = var.workload_identity_pool_id
  github_owner              = var.github_owner
  github_repo               = var.github_repo
  service_account_email     = module.deployer_sa.service_account_email
  depends_on = [ module.deployer_sa, module.apis]
}

module "artifact_registry" {
  source        = "../../infra/gcp-iac/modules/artifact_registry"
  repository_id = var.repository_id
  region        = var.region
  depends_on = [ module.apis ]
}