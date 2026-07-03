# Message Drafter

Message Drafter is a Python-based cloud-native project for generating and sending draft greetings to personal acquaintances on a schedule. It leverages Google Cloud Run, Firestore, Artifact Registry, and is fully managed via Infrastructure as Code (Terraform) and CI/CD pipelines (GitHub Actions).

Each run generates a short, casual Swedish greeting (starting with the slang "Tja") using Claude, delivers it to a Telegram chat, and records it in Firestore so future drafts don't repeat recent messages.

---

## Features
- **Automated Message Drafting:** Uses Anthropic's Claude to generate short, friendly Swedish greetings.
- **Scheduled Delivery:** Runs as a scheduled Cloud Run Job, triggered daily by Cloud Scheduler.
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
│   ├── llm_service.py       # LLM (Anthropic Claude) integration
│   └── storage_service.py   # Firestore integration
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container definition
├── secrets.env              # Local development secrets (not committed)
├── terraform/               # Infrastructure as Code
│   ├── main.tf              # Main Terraform config
│   ├── variables.tf         # Input variables
│   ├── output.tf            # Outputs
│   ├── terraform.tfvars.example  # Example variable values
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
- Create a `terraform/terraform.tfvars` with your project details (copy from `terraform/terraform.tfvars.example`).

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
ANTHROPIC_API_KEY=your-anthropic-api-key
PROJECT_ID=your-gcp-project-id
DB_NAME=your-firestore-database-id
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
- On push to `master` or `feature/*` (ignoring `*.md`, `*.txt`, and `.gitignore` changes), or via manual `workflow_dispatch`, the workflow in `.github/workflows/deploy.yml`:
  - Authenticates to GCP using Workload Identity Federation
  - Builds and pushes the Docker image to Artifact Registry
  - Deploys the Cloud Run Job (`daily-could-run-job-deployed`) with the required environment variables
  - Creates or updates a Cloud Scheduler job that triggers the run daily at 12:00 `Europe/Stockholm`

Secrets are managed in GitHub repository settings.

---

## Usage
- The job fetches the 5 most recent drafts from the Firestore `drafts` collection, generates a new Swedish greeting with Claude (avoiding recent messages), sends it to Telegram, and stores the new draft.
- To trigger manually, run `python src/main.py` locally (with `secrets.env` set), or use the **Run workflow** button on the GitHub Actions workflow.

---

## Extending & Testing
- Adjust the prompt or model in `llm_service.py` (currently uses `claude-sonnet-4-6`).
- Change chat integration in `chat_service.py`.
- Add more storage backends in `storage_service.py`.

---

## License
No license.

---

## Author
Medet Kiflemariam
