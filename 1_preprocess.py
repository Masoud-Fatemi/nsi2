#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 13:44:46 2025

@author: masoud
"""
import pandas as pd

save = False
country = 'au'
# country = 'uk'
# country = 'us'

df = pd.read_csv('data/df.csv')
df = df[df['country']==country]
country_df = pd.read_csv(f'data/{country}.csv')

"""combine csv and rename columns"""
columns_new_names = {
    'userids': 'networkID',
    'interactions':'IS',
    'interactions_p':'RIS',
    'betweenness_mean': 'ABC', 
    'betweenness_range':'RBC',
    'closeness':'ACC',
    'social_similarities':'SocSim',
    'outliers':'OUT',
    'densities':'DENS'
    }
# Rename columns
country_df.rename(columns=columns_new_names, inplace=True)
country_df['IS'] = country_df['IS'].fillna(0)

# Adding nsi lable
country_df = country_df.merge(
    df[["userids", "alpha-8"]],
    left_on="networkID",
    right_on="userids",
    how="left"
)
# Drop duplicate userids column
country_df.drop(columns="userids", inplace=True)
country_df.rename(columns={'alpha-8':'nsi'}, inplace=True)

if save:
    country_df.to_csv(f'output/{country}.csv', index=False)