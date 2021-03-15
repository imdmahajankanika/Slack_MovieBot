################## Execute this file firstly before starting "MovieBot" to store the variables in storedVar.joblib file ##################
"""
This onetime setup makes it easier in situations when the data is changing constantly and the bot needs to adapt to these data changes quickly.
All we need to do is to run this file whenever we need without changing any of the internal functions in the bot.
cd
"""

import joblib
import pandas as pd
import os,sys
import nltk
from config import storedVarFile
from recommendation import *

if __name__ == "__main__":

    metadata = pd.read_csv('movies_metadata_prep.csv')
    
    ########      Metadata based collobarative filtering  #############    
    
    documents = metadata['overview'].fillna('')
    cosine_sim = metadata_filtering(documents)
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    
    ########## Search title based on keywords  #############
    
    documents = list(metadata['title'].fillna(''))
    tfidf_fit, tfidf_matrix = tfidf_fit(documents)

    ########### Store the variables to a joblib file #############

    i = [cosine_sim,indices,tfidf_fit, tfidf_matrix]
    joblib.dump(i,storedVarFile,compress=('lz4', 9))
    
    