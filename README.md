# Message Drafter

#### MVP:
Currently we are at the MVP stage, where the solution exists on the cloud and is scheduled, nothing more:
- Python script that outputs a message draft. Does not need to be LLM generated.
- Cloudize & Scheduling: Google Cloud Run for hosting the script, chedule job once daily.

#### Todo:
To get further, we want to add a few features:
1. CI/CD: Develop & test locally, deploy to prod that runs on cloud.
    - Put secrects in GH
    - Write a workflow that deploys resources.
2. Get code to work with an LLM API!
3. Logging: Store previously sent messages so they dont get sent again.
4. Personalization:
    - Test if LLM can use a sample activity logg written manually.
    - Connect to my Apple Calender - https://github.com/jazzband/icalevents, see if possible to create daily summaries.
