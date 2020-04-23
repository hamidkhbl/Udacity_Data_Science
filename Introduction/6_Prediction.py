import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('survey_results_public.csv')

df.hist()
#plt.show()

sns.heatmap(df.corr(), annot=True, fmt='.2f')
#plt.show()

#remove null values
df = df.dropna()

X = df[['JobSatisfaction','CareerSatisfaction', "HoursPerWeek"]]
Y = df['Salary']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=42)


#instansiate
lm = LinearRegression(normalize=True)
#fit
lm.fit(X_train, Y_train)
#preditct
y_test_preds = lm.predict(X_test) 
#score
"The r-squared score for your model was {} on {} values.".format(r2_score(Y_test, y_test_preds), len(Y_test))