import slack
import os

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
"""
#  Hello World Program
response = client.chat_postMessage(
    channel='CKTEXR9AL',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"
"""

array = client.channels_list()
for x in array['channels']:
    print(x['id'])
