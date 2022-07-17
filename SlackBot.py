import slack
import os
from pathlib import Path
from dotenv import load_dotenv

# set project root path
root_path = Path('.') / '.env'
load_dotenv(dotenv_path=root_path)

# set access key for your own slack app
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# send message
client.chat_postMessage(channel='#alarm', text='[BOT]Test message from custom bot')