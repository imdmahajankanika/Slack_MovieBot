####################### Configurations for Slack MovieBot and IBM Watson service  ##########################

import os
import watson_developer_cloud
from slackclient import SlackClient
 

################# Slack configuration   ##########################

SLACK_BOT_TOKEN='xoxb-1849778358129-1864408962976-vQYi95DB6pBvLyYWkRWxnHAp'
SLACK_VERIFICATION_TOKEN='sxTkZCZFqMczL4AC0SWt6Udw' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

##################### Watson service configuration   ##########################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'e5qmHc5bqrepemq4tsjUxaO4oQeAJTQ9nydWuaHPLCD0', # Assistant APIKey
    version = '2020-04-01'
)

assistant_id = '15bff5b1-2f4c-4cc2-a1a6-4d9340efd3e2' # Assistant Skill ID


######## Temporary file configuration ###############
storedVarFile = "nlp/recommendation_Sys/storedVar.joblib" 
