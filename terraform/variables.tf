variable "project_id" {
  type = string
}
variable "project_number" {
  type = string
}
variable "required_apis" {
  description = "List of APIs to enable for the project"
  type        = list(string)
}
variable "deployer_sa_roles" {
  description = "List of roles to give the Deployer SA"
  type = list(string)
}
variable "runtime_sa_roles" {
  description = "List of roles to give the Runtime SA"
  type = list(string)
}
variable "region" {
  type = string
}
variable "user_email" {
  type = string
}
variable "id_github_sa" {
  description = "ID of Service Account used to in Github Actions."
  type = string
}
variable "id_runtime_sa" {
  description = "ID of Service Account used in runtime of Cloud Run Job."
  type = string
}
variable "repository_id" {
  description = "Artifact Registry Repository ID."
  type = string
}
variable "workload_identity_pool_id" {
  description = "ID of the Github pool for Workload Identity Federation."
  type = string
}
variable "github_owner" {
  type = string
}
variable "github_repo" {
  type = string
}
variable "firestore_db_name" {
  type = string
}