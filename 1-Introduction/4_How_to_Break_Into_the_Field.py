import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('survey_results_public.csv')

study = df['CousinEducation'].value_counts().reset_index()

study.rename(columns={'index':'method', 'CousinEducation':'count'}, inplace=True)
#print(study.head())


possible_values = set()
study['method'].apply(lambda x : [possible_values.add(item) for item in x.split(';')])
print(possible_values)




