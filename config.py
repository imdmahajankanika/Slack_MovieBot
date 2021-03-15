####################### Configurations for Slack MovieBot and IBM Watson service  ##########################

import os
import watson_developer_cloud
from slackclient import SlackClient
from ibm_watson import AssistantV2
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

"""version='2020-09-24'
apikey='e5qmHc5bqrepemq4tsjUxaO4oQeAJTQ9nydWuaHPLCD0'
service_url=os.environ.get('WATSON_API_URL')
assistant_id='8a7b890d-a52e-44b3-953f-6d46a6700853'
"""

################# Slack configuration   ##########################

SLACK_BOT_TOKEN='xoxb-1849778358129-1864408962976-kOfd2vSSFAPc1AOcf8u0RhMY'
SLACK_VERIFICATION_TOKEN='sxTkZCZFqMczL4AC0SWt6Udw' 

# Instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) 

##################### Watson service configuration   ##########################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'e5qmHc5bqrepemq4tsjUxaO4oQeAJTQ9nydWuaHPLCD0', # Assitant APIKey
    version = '2020-04-01'
)

assistant_id = '15bff5b1-2f4c-4cc2-a1a6-4d9340efd3e2' # Assistant skill ID


"""authenticator = IAMAuthenticator(apikey)
assistant = AssistantV2(
    version=version,
    authenticator=authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')
assistant.set_disable_ssl_verification(True)
"""

