import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

class SlackBot:
    def __init__(self):
        # set project root path
        root_path = Path('.') / '.env'
        load_dotenv(dotenv_path=root_path)

        # set access key for your own slack app
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    
    def send_message(self, message):
        # send message
        res = self.client.chat_postMessage(channel='#alarm', text=message)
        if res.status_code == 200:
            print("message sent successfully!")
        else:
            print(f"Failed to send message with error code {res.status_code}")
        return res
