# Run this code cell to install and import the pycountry library
#!pip install pycountry
from pycountry import countries
import pandas as pd

# Run this code cell to see an example of how the library works
countries.get(name='Spain')

# Run this code cell to see how you can also look up countries without specifying the key
countries.lookup('Kingdom of Spain')


#encoding
from encodings.aliases import aliases

alias_values = set(aliases.values())

# This code finds the encodings that works for the file
for encoding in set(aliases.values()):
    try:
        df=pd.read_csv("mystery.csv", encoding=encoding)
        print('successful', encoding)
    except:
        pass

# Fill null
# Fill with mean of a group

df_melt = pd.read_csv('gdp_data.csv')
df_melt['GDP_filled'] = df_melt.groupby('Country Name')['GDP'].transform(lambda x: x.fillna(x.mean()))

# Forward fill
df_melt['GDP_ffill'] = df_melt['GDP'].fillna(method = 'ffill')

# Bakward fill
df_melt['GDP_bfill'] = df_melt['GDP'].fillna(method = 'backfill')

