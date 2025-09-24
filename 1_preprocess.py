#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 13:44:46 2025

@author: masoud
"""
import pandas as pd

save = True
df = pd.read_csv('data/df.csv')
df = df[df['country']=='uk']
uk = pd.read_csv('data/uk.csv')

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
uk.rename(columns=columns_new_names, inplace=True)
uk['IS'] = uk['IS'].fillna(0)

# Adding nsi lable
uk = uk.merge(
    df[["userids", "alpha-8"]],
    left_on="networkID",
    right_on="userids",
    how="left"
)
# Drop duplicate userids column
uk.drop(columns="userids", inplace=True)
uk.rename(columns={'alpha-8':'nsi'}, inplace=True)

if save:
    uk.to_csv('output/uk.csv', index=False)