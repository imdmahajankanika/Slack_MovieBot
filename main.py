################ Main program #################

import os,string
import time
import datetime
from slack.slack_events import parse_bot_events, send_response
from config import slack_client
from nlp.nlp_events import handle_response
import pandas as pd
import json

# Initialization...
context = {}
current_action = ''
#stores the session details of each user
session_details = pd.DataFrame({},columns=['timestamp', 'user', 'context']) 
# user ID will be assigned to MovieBot user, once the MovieBot starts up
botId = None

# Delay between Real Time Messaging...
RTM_READ_DELAY = 1 

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("MovieBot connected and running!")
        
        # Get MovieBot user ID using Web API method
        botId = slack_client.api_call("auth.test")["user_id"]
        # Keeping the section active...
        while True:
            # Get details from real time messaging
            userId,current_user,msg,team,channel,start_ts  = parse_bot_events(slack_client.rtm_read(),botId) 
            # If current user types message in Slack MovieBot
            if msg: 
                try:
                    context = json.loads(session_details.loc[session_details.user == current_user+channel,'context'].values[0])
                    #print("context",context)
                except:
                    context = {}
                    session_details = session_details.append({'timestamp': start_ts, 'user': current_user+channel, 'context': json.dumps(context)}, ignore_index=True)
                # Handling the input message received by current user...
                context,slack_output,current_action = handle_response(msg,channel, current_user,context) 
                print("\n",current_user,":",msg,"\nContext:- ",context,"\n\nMovieBot: ",slack_output)
                session_details.loc[session_details.user == current_user+channel,'context'] = json.dumps(context) 
                # Sending output message back to current user                
                send_response(channel, slack_output) 
                conversation_id = context['conversation_id']
                
                # Reset context when intent is '#Goodbye'
                if current_action == 'end_conversation': 
                    #print(current_action)
                    session_details = session_details[session_details.user != current_user+channel]
                    context = {}
                    current_action = ''
                
                end_ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                processing_time = str((datetime.datetime.strptime(end_ts, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(start_ts, '%Y-%m-%d %H:%M:%S')).total_seconds())
                
            time.sleep(RTM_READ_DELAY)
    else:
        print("Oops! Connection failed! Check the above Traceback!")