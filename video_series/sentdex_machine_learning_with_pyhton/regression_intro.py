# Idea of regression is to take data and try to fit best line

import pandas as pd 
import quandl

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]


# This is how you could add a column using others
df['HL_PCT'] = (df['Adj. High'] - df ['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head())

# Some people are avid believers of pattern recognition in stock prices,
# but you probably will not need all the features. It is about
# using valueable features!

# Features are the attributes that make up the label
# The label should be (hopefully) some prediction of the future



