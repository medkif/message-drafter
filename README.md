# Message Drafter

#### MVP:
Currently we are at the MVP stage, where the solution exists on the cloud and is scheduled, nothing more:
- Python script that outputs a message draft. Does not need to be LLM generated.
- Cloudize & Scheduling: Google Cloud Run for hosting the script, chedule job once daily.

#### Todo:
To get further, we want to add a few features:
- CI/CD: Develop & test locally, deploy to prod that runs on cloud? probably need Docker and stuff.
    - Put secrects in GH
    - Write a workflow that deploys resources.
- Get code to work with an LLM API!
- Logging: Store previously sent messages so they dont get sent again.
- Personalization: Connect to my Apple Calender - https://github.com/jazzband/icalevents