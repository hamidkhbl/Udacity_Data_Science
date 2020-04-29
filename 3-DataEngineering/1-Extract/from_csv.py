import pandas as pd

df_projects = pd.read_csv('projects_data.csv', dtype = str)
df_population = pd.read_csv('population_data.csv', skiprows=4)
# dtype = str means get all the data as string. It can be a dictionary for each column.

#count the number of null values in the data set (each column)
df_projects.isnull().sum()
df_projects.isnull().sum() / df_projects.shape[0]

#count the number of null values in the data set (each row)
df_population.isnull().sum(axis=1)
df_population[df_population.isnull().any(axis=1)]

# read first 10 lines of the file
f = open('population_data.csv')
for l in range(10):
    line = f.readline()
    print(l, line)
f.close()

# skip first 4 rows
df_population = pd.read_csv('population_data.csv', skiprows=4)