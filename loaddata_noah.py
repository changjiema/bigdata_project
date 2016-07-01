# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:11:02 2016

@author: PBM887

reads in all json files from a folder as python dictionaries
"""

import os
import json
import pandas as pd
#from pprint import pprint
# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
META_DIR = os.path.join(DATA_DIR, 'metacritic')



def load_movie_data():
    movie_list_mojo=[]
    movie_list_meta=[]

    for file1 in os.listdir(MOJO_DIR):
        path=MOJO_DIR+'\\'+file1
        with open(path, 'r') as target_file:
            movie = json.load(target_file)
            movie_list_mojo.append(movie)
            
    for file1 in os.listdir(META_DIR):
        if '_parsed' in str(file1):
            path=META_DIR+'\\'+file1
            with open(path, 'r') as target_file:
                movie = json.load(target_file)
                movie_list_meta.append(movie)
    #print 6
    return movie_list_mojo,movie_list_meta

mojo,meta=load_movie_data()[0],load_movie_data()[1]



for i in meta:
    i['num_critic_reviews']=str(i['num_critic_reviews'])
    i['num_user_reviews']=str(i['num_user_reviews'])
    
meta_df=pd.DataFrame(meta)
mojo_df=pd.DataFrame(mojo)

both_df=pd.merge(mojo_df,meta_df, on='title',how='left')
#==============================================================================
# 
# pd.merge()
# 
# meta_df.num_critic_reviews.head
# 
# 
#==============================================================================
