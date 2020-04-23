import numpy as np 
import pandas as pd 

schema = pd.read_csv('survey_results_schema.csv')
df = pd.read_csv('survey_results_public.csv')

print(schema[schema['Column'] == 'CareerSatisfaction']['Question'].item())
print(schema[schema['Column'] == 'JobSatisfaction']['Question'].item())

print(schema[schema['Column'] == 'CousinEducation']['Question'].item())

