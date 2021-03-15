################# NLP event analysis  ######################

"""
    Handles the nlp events received from IBM Watson service
"""

import os,sys
sys.path.append(os.path.normpath(os.getcwd()))
import random
from config import service, assistant_id
from nlp.recommendation_Sys.recommendation import *
import pandas as pd
from slack.slack_events import msg_tiles, msg_buttons

def handle_response(msg, channel, current_user,context):
    """
        NLP analysis on top of the conversation
    """
    current_action = '' # Intialize current action to empty
    slack_output = ''   # Intialize Slack output to empty
    
  # Send message to Assistant service.
    response = service.message(
    workspace_id = assistant_id,
    input = {'text': msg},
    context = context).get_result()
    #print("response:-  ",response) 
    try:
        slack_output = ''.join(response['output']['text'])
        #print("\nslack_output", slack_output)
        
    except:
        slack_output = ''
    
  # Update the last context with the recent context from the IBM watson dialog
    context = response['context']
    #print(context, response)

    ###########  Identify the search_item  ###########
    try:
        search_key = response['entities'][0]['value']
    except:
        search_key = ''
    
    try:
        search_item = str(response['context']['movie_name'])    
    except:
        search_item = ''
        
    res = ''
    

    ###########  Prepare response for movie selection from 5 results ###########    
    try:
        if response['context']['currentIntent'] == 'hello' and search_item.strip() != '' and str(response['context']['option']) in ['1','2','3','4','5']:
            
            selection = int(response['context']['option']) - 1
            b = similarity_search(search_item, list(metadata.index))
            response['context']['movie_name'] = metadata.loc[b]['title'].values[selection]
            search_item = ''
    except:
        pass

    ###########  Prepare response for movies search  ###########    
    try:
        if response['context']['currentIntent'] == 'hello' and search_item.strip() != '':
            
            b = similarity_search(search_item, list(metadata.index))
            results, links = metadata.loc[b]['title'], metadata.loc[b]['imdbURL']
            msg_buttons(channel, results, links, 'Showing below results for "' + str(search_item) + '"')
    except:
        pass

    ###########  Prepare response for recommending similar movies ###########    
    try:
        if response['context']['currentIntent'] == 'recommend_movies':
            
            a = get_recommendations(search_item)
            title, title_url, image_url = a, metadata.loc[a.index]['imdbURL'], metadata.loc[a.index]['ImageURL']
            msg_tiles(channel, search_item, title, title_url, image_url)
        
        
    except:
        pass
    
    ###########  Prepare response for avg votes for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'votes':
            res = str(metadata[metadata['title'] == search_item]['vote_average'].values[0])
    except:
        pass
    
    ###########  Prepare response for query regarding adult content ###########    
    try:
        if response['context']['currentIntent'] == 'adult_content':
            if metadata[metadata['title'] == search_item]['adult'].values[0] == 'True':
                res = "It's an adult movie! It's not recommended to watch it with kids!"
            else:
                res = "It's not an adult movie! You can watch it with kids!"
    except:
        pass
    
    ###########  Prepare response for movie genre ###########    
    try:
        if response['context']['currentIntent'] == 'genre':
            res = str(metadata[metadata['title'] == search_item]['genres'].values[0])
    except:
        pass
    
    ###########  Prepare response for revenue for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'revenue':
            res = '$' + "{:,}".format(int(metadata[metadata['title'] == search_item]['revenue'].values[0])) 
    except:
        pass
    
    ###########  Prepare response for overview for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'overview':
            res = str(metadata[metadata['title'] == search_item]['overview'].values[0]) 
    except:
        pass
    
    ###########  Prepare response for imdb link for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'imdb':
            res = str(metadata[metadata['title'] == search_item]['imdbURL'].values[0]) 
    except:
        pass
    
    ###########  Prepare response for tmdb link for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'tmdb':
            res = str(metadata[metadata['title'] == search_item]['tmdbURL'].values[0]) 
    except:
        pass
    
    ###########  Prepare response for budget for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'budget':
            res = '$' + "{:,}".format(int(metadata[metadata['title'] == search_item]['budget'].values[0]))
    except:
        pass
    
    ###########  Prepare response for vote count for the selected movie ###########    
    try:
        if response['context']['currentIntent'] == 'vote_count':
            res = "{:,}".format(int(metadata[metadata['title'] == search_item]['vote_count'].values[0]))
    except:
        pass


    if slack_output == '' and search_item.strip() == '':
        slack_output = "Search results not found! Please re-try!" 
    
    if 'actions' in response:
        if response['actions'][0]['type'] == 'client':
            current_action = response['actions'][0]['name']
        #print("current action", current_action)
        # if current action is end of the conversation
        slack_output = slack_output

    else:
        slack_output = slack_output + str(res)

    return(context,slack_output,current_action)