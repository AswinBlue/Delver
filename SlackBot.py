import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter


# set project root path
root_path = Path('.') / '.env'
load_dotenv(dotenv_path=root_path)

# set access key for your own slack app
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# send message
client.chat_postMessage(channel='#alarm', text='[BOT]Test message from custom bot')

# set event adapter
server = Flask('Delver')
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SECRET'],'/slack/events', server)
server.run()
# @slack_event_adapter.on('message')
