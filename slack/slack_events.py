############# Slack messages processing #################  

import os
import time
import re
from slackclient import SlackClient
from config import slack_client
import datetime

direct_mention_regex = "^<@(|[WU].+?)>(.*)"

def parse_bot_events(slack_events,botId):
    """
        Parses the list of events coming from the Slack RTM API to find bot commands
        and returns conversation details else returns None, None.
    """
    for event in slack_events:
        #print("\n\n\n",event)
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == botId:
                message_user = event['user']
                team = event['team']
                channel = event['channel']
                start_ts = datetime.datetime.fromtimestamp(float(event['event_ts'])).strftime('%Y-%m-%d %H:%M:%S')
                return user_id,message_user,message,team,channel,start_ts
    return None, None, None, None, None, None
    
#Finds a direct mention @Moviebot in chatbox to ensure that we are chatting with chatbot not any other user
def parse_direct_mention(event_message):
    # Match the pattern...
    matches = re.search(direct_mention_regex, event_message)
    # Group 1 contains the username (@MovieBot) and group2 contains the remaining message from current user
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

# Send response message back to current user
def send_response(channel,slack_output):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=slack_output
    )

# Organize the bot response in tiles format
def msg_tiles(channel, search_item, title, title_url, img_url):
    attachment_json = [
            {
                "title": title.values[0],
                "title_link": title_url.values[0],
                "image_url": img_url.values[0]
            },
            {
                "title": title.values[1],
                "title_link": title_url.values[1],
                "image_url": img_url.values[1]
            },
            {
                "title": title.values[2],
                "title_link": title_url.values[2],
                "image_url": img_url.values[2]
            }
        ]
  
    # Send response with the above attachment, showing user the recommendations for movies
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text='Recommendations for movies similar to "' + str(search_item) + '"',
      attachments=attachment_json
    )      
#Organize the response in button format     
def msg_buttons(channel, results, links, search_item):
    attachment_json = [
        {
            "text": " ",
            "fallback": "You didn't make a selection",
            "callback_id": "code_search",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "code_link",
                    "text": "1. " + results.values[0],
                    "type": "button",
                    "url": links.values[0]
                },
                {
                    "name": "code_link",
                    "text": "2. " + results.values[1],
                    "type": "button",
                    "url": links.values[1]
                },
                {
                    "name": "code_link",
                    "text": "3. " + results.values[2],
                    "type": "button",
                    "url": links.values[2]
                },
                {
                    "name": "code_link",
                    "text": "4. " + results.values[3],
                    "type": "button",
                    "url": links.values[3]
                },
                {
                    "name": "code_link",
                    "text": "5. " + results.values[4],
                    "type": "button",
                    "url": links.values[4]
                }
            ]
        }
    ]

    # Send response with the above attachment and ask the current user for selecting options
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text=search_item,
      attachments=attachment_json
    )