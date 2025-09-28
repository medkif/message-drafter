# Message Drafter
Message Drafter is a personal project for generating draft greetings that can be sent to personal acqaintances.

##### Status:
Currently we are at the MVP stage, where the solution exists on the cloud and is scheduled, nothing more:
- Python script that outputs a message draft. Does not need to be LLM generated.
- Cloudize & Scheduling: Google Cloud Run for hosting the script, schedule job once daily.

#### Todo:
To get further, we want to add a few features:
1. Get code to work with an LLM, either API or local!
2. Logging: Store previously sent messages so they dont get sent again.
3. Personalization:
    - Test if LLM can use a sample activity logg written manually.
    - Connect to my Apple Calender - https://github.com/jazzband/icalevents, see if possible to create daily summaries.
