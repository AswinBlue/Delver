# Slack bot
- template for bot in Slack

## installation
1. create slack app
  - go to 'https://api.slack.com/apps' and create new app
  - set authority to functions for bot
  - apply your bot to your slack
  - goto "Oauth & Permission page" and get "Bot User OAuth Token"
2. set Key
  - you need to set api Key, get "Bot User OAuth Token" by following "1. create slack app"
  - create .env file in root path of the project and type SLACK_TOKEN = <YOUR_KEY>
  - replace `<YOUR_KEY>` with "Bot User OAuth Token"
3. set event subscription
  - go to 'https://api.slack.com/apps/', and click your own app
  - at 'Event Subscriptions' tab, check 'enable events'
  - run your python code, and click verify 'request URL' with your URL (your code must have 'SlackEventAdapter' sentence)
  - add event you want to subscribe to event list
4. create code
  - use methods in 'SlackBot.py' to control slack bot
  - use 'WebScrapper.py' to scrap web pages
