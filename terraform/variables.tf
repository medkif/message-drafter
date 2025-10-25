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
variable "sa_roles" {
  description = "List of roles to give the Service Account(s)"
  type = list(string)
}
variable "region" {
  type = string
}
variable "user_email" {
  type = string
}
variable "service_account_id" {
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
