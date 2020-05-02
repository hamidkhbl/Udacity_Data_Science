# Read a file line by line
def print_lines(n, file_name):
    f = open(file_name)
    for i in range(n):
        print(i, f.readline())
    f.close()

import pandas as pd
df_json = pd.read_json('population_data.json', orient = 'records')

'''
options for orient:

    'split' : dict like {index -> [index], columns -> [columns], data -> [values]}

    'records' : list like [{column -> value}, ... , {column -> value}]

    'index' : dict like {index -> {column -> value}}

    'columns' : dict like {column -> {index -> value}}

    'values' : just the values array

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
'''