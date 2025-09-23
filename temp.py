# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 23:25:22 2025

@author: Masou
"""
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')

columns = [
 'DENS',
 'OUT',
 'SS',
 'IS',
 'RIS',
 'ABC',
 'RBC',
 'ACC',
 'nsi']

"""Correlation Analysis"""
corr = df[columns].corr()["nsi"].sort_values(ascending=False)
print("\nCorrelation:")
print(round(corr[1:], 2))


"""Linear Regression Coefficients"""
X = df[[ 'DENS','OUT', 'SS', 'IS', 'RIS', 'ABC', 'RBC', 'ACC',]]
y = df["nsi"]
model = LinearRegression().fit(X, y)
importance_series = pd.Series(model.coef_, index=X.columns)
importance  = importance_series.sort_values(ascending=False)
print("\nRegression:")
print(round(importance, 3))

