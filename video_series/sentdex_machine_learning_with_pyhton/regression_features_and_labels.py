import pandas as pd 
import quandl
import math

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]


df['HL_PCT'] = (df['Adj. High'] - df ['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

#You do this so in the future you could change what you want to forecast
forecast_col = 'Adj. Close'

# You can do this to fill data you don't have with a value that will be 
# treated as an outlier. This will generally be preferable to just throwing
# some of your data ouit because you are missing only one column
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))

# This will shift the columns with the label (in this case Adj. Close) up
# by the length of forecast_out. This allows us to use data from a certain
# day to predict the stock price in that length of days from now instead of
# the same day.
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())


# You can't really use Adj. Close as a label, for example, because other
# features were derived from it.