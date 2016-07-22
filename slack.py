import json
from configure import get_args
from slackclient import SlackClient

slack_client = None

def init():
    global slack_client

    with open('config.json') as data_file:
        data = json.load(data_file)

        api_key = _str( data["slack_api_token"] )
        if api_key:
            slack_client = SlackClient(api_key)

# Safely parse incoming strings to unicode
def _str(s):
    return s.encode('utf-8').strip()

def sendPostMsg(notification_text, notification_attachment=None, channels=None):
    for channel in channels:
        slack_client.api_call("chat.postMessage", channel=channel, as_user=True, text=notification_text, attachments=notification_attachment)

init()
