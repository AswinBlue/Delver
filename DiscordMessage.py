import requests
import os
from pathlib import Path
from dotenv import load_dotenv

def send_message(text):
    # set project root path
    root_path = Path('.') / '.env'
    load_dotenv(dotenv_path=root_path)

    # set access key for your discord channel by 

    data = {
        "content" : text,
        "username" : "Delver"
    }
    res=requests.post(os.environ['DISCORD_URL'], json=data)
    if res.status_code == 200:
        print("message sent successfully!")
    else:
        print(f"Failed to send message with error code {res.status_code}")
    return res