import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from Dummy_variables import create_dummy_df

df = pd.read_csv('survey_results_public.csv')

df.hist()
#plt.show()

sns.heatmap(df.corr(), annot=True, fmt='.2f')
#plt.show()

df = df[['CareerSatisfaction', 'HoursPerWeek', 'JobSatisfaction', 'StackOverflowSatisfaction','Salary']]
#remove null values
df = df.dropna(subset=['Salary'], axis=0)

# Fill the mean
fill_mean = lambda col: col.fillna(col.mean())
df = df.apply(fill_mean, axis=0)

X = df[['CareerSatisfaction', 'HoursPerWeek', 'JobSatisfaction', 'StackOverflowSatisfaction']]
Y = df['Salary']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=42)

#instansiate
lm = LinearRegression(normalize=True)
#fit
lm.fit(X_train, Y_train)
#preditct
y_test_preds = lm.predict(X_test) 
#score
print("The r-squared score for your model was {} on {} values.".format(r2_score(Y_test, y_test_preds), len(Y_test)))

# prediction using dummy variables
df = create_dummy_df(df, ['CareerSatisfaction', 'HoursPerWeek', 'JobSatisfaction', 'StackOverflowSatisfaction'], False)

X = df.drop('Salary', axis=1)
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)

#instansiate
lm = LinearRegression(normalize=True)
#fit
lm.fit(X_train, Y_train)
#preditct
y_test_preds = lm.predict(X_test) 
#score
print("The r-squared score for your model was {} on {} values.".format(r2_score(Y_test, y_test_preds), len(Y_test)))
