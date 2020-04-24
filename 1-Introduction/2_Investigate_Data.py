#%%
import pandas as pd 
import numpy as numpy 
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('survey_results_public.csv')
df.head()

#%%
# Find columns that has no missing value
no_nulls = df.columns[(df.isnull().mean() == 0) == True]
print(no_nulls)

# Find columns that has more than 75% missing value
missing_75 = df.columns[(df.isnull().mean() > 0.75) == True]
print(missing_75)

#%%
# top 10 countries
countries = df.Country.value_counts()[:10]
countries.plot(kind = 'bar')
plt.show()
# %%
