#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:41:41 2025

@author: masoud
"""

from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('output/uk.csv')
columns = [
 'DENS',
 'OUT',
 'SocSim',
 'IS',
 'RIS',
 'ABC',
 'RBC',
 'ACC',
 'nsi']

matrix = df[columns].corr()

plt.figure(figsize=(8,6))
sns.heatmap(matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()