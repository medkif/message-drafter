# Message Drafter

Message Drafter is a Python-based cloud-native project for generating and sending draft greetings to personal acquaintances on a schedule. It leverages Google Cloud Run, Firestore, Artifact Registry, and is fully managed via Infrastructure as Code (Terraform) and CI/CD pipelines (GitHub Actions).

---

## Features
- **Automated Message Drafting:** Uses OpenAI to generate friendly greetings.
- **Scheduled Delivery:** Runs as a scheduled Cloud Run Job, triggered by Cloud Scheduler.
- **Cloud-Native:** All infrastructure is provisioned via Terraform.
- **CI/CD:** Automated build and deployment using GitHub Actions and Workload Identity Federation.
- **Persistent Storage:** Stores sent drafts in Firestore to avoid repetition.
- **Telegram Integration:** Sends messages to a Telegram chat via bot.

---

## Project Structure
```
├── src/
│   ├── main.py              # Entry point for the job
│   ├── chat_service.py      # Telegram integration
│   ├── llm_service.py       # LLM (OpenAI) integration
│   └── storage_service.py   # Firestore integration
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container definition
├── secrets.env              # Local development secrets (not committed)
├── terraform/               # Infrastructure as Code
│   ├── main.tf              # Main Terraform config
│   ├── variables.tf         # Input variables
│   ├── output.tf            # Outputs
│   ├── terraform.tfvars     # Variable values (example)
│   └── versions.tf          # Provider versions
└── .github/workflows/       # GitHub Actions CI/CD
```

---

## Prerequisites
- Python 3.11+
- Docker
- Google Cloud account & project
- Terraform >= 1.0.0
- [gcloud CLI](https://cloud.google.com/sdk/docs/install)
---

## Step-by-Step Setup

### 1. Clone the repository
```sh
git clone https://github.com/medkif/message-drafter.git
cd message-drafter
```

### 2. Set up Google Cloud Project
- Create a new GCP project or use an existing one.
- Enable the required APIs:
  - Artifact Registry
  - IAM
  - Compute Engine
  - Cloud Run
  - Cloud Build
  - Cloud Scheduler
  - Firestore
- Create a Firestore database in Native mode.

### 3. Configure Terraform
- Create a `terraform/terraform.tfvars` with your project details (use the .tfvars.ezample file).

### 4. Initialize and Apply Terraform
```sh
cd terraform
terraform init
terraform apply
```
- This will provision all required GCP resources.

### 5. Set up GitHub Actions Secrets
- In your GitHub repository, add the necessary secrets for CI/CD (see `.github/workflows/deploy.yml` for required secrets).
- Typical secrets include GCP Workload Identity Federation configuration.

### 6. Configure Local Environment
- Create a `secrets.env` file in the project root:
```env
BOT_TOKEN=your-telegram-bot-token
CHAT_ID=your-telegram-chat-id
OPENAI_API_KEY=your-openai-api-key
PROJECT_ID=your-gcp-project-id
```

### 7. Install Python Dependencies
```sh
pip install -r requirements.txt
```

### 8. Run Locally (for testing)
```sh
python src/main.py
```

---

## Infrastructure (Terraform)
All GCP resources (Cloud Run, Firestore, Artifact Registry, Service Accounts, IAM, Scheduler) are managed via Terraform in the `terraform/` directory.

### 1. Configure Terraform Variables
Edit `terraform/terraform.tfvars` with your project details.

### 2. Initialize & Apply
```sh
cd terraform
terraform init
terraform apply
```

---

## CI/CD (GitHub Actions)
- On push to `master` or `feature/*`, the workflow in `.github/workflows/deploy.yml`:
  - Authenticates to GCP using Workload Identity Federation
  - Builds and pushes Docker image to Artifact Registry
  - Deploys to Cloud Run Job
  - Schedules the job with Cloud Scheduler

Secrets are managed in GitHub repository settings.

---

## Usage
- The job fetches recent drafts from Firestore, generates a new greeting using OpenAI, sends it to Telegram, and stores the new draft.
- To trigger manually, run `python src/main.py` locally (with `secrets.env` set).

---

## Extending & Testing
- Add new message logic in `llm_service.py`.
- Change chat integration in `chat_service.py`.
- Add more storage backends in `storage_service.py`.
- For local LLM, use the `ollama_local` or `ollama_api` functions.

---

## License
No license.

---

## Author
Medet Kiflemariam
