# Pandas and sqlite3

import sqlite3
import pandas as pd

# connect to the database
conn = sqlite3.connect('population_data.db')

# run a query
pd.read_sql('SELECT * FROM population_data', conn)

# SQLAlchemy and Pandas
# https://docs.sqlalchemy.org/en/13/core/engines.html

import pandas as pd
from sqlalchemy import create_engine

### 
# create a database engine 
# to find the correct file path, use the python os library:
# import os
# print(os.getcwd())
#
###

engine = create_engine('sqlite:////home/workspace/3_sql_exercise/population_data.db')
pd.read_sql("SELECT * FROM population_data", engine)

pd.read_sql('SELECT "1961","1960" FROM population_data where Country_Name = "Aruba"', engine)
