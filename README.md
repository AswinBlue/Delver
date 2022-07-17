# Slack bot
- template for bot in Slack

## installation
1. go to 'https://api.slack.com/apps' and create new app
  - set authority to functions for bot
  - apply your bot to your slack
  - get unique Key 

1. set Key
  - you need to set api Key, you got from (1), into your code
  - create `.env` file in root path of the project and type `SLACK_TOKEN = <YOUR_KEY>`
  - set secret key in `.env` as `SLACK_SECRET = <YOUR_SECRET_KEY>`

1. create code
  - in 'SlackBot.py', code your business logic 

1. set event subscription
  - go to 'https://api.slack.com/apps/', and click your own app
  - at 'Event Subscriptions' tab, check 'enable events'
  - run your python code, and click verify 'request URL' with your URL (your code must have 'SlackEventAdapter' sentence)
  - add event you want to subscribe to event list
