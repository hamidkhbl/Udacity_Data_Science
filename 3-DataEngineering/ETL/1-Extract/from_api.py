import requests
import pandas as pd

url = 'http://api.worldbank.org/v2/countries/br;cn;us;de/indicators/SP.POP.TOTL/?format=json&per_page=1000'
r = requests.get(url)

pd.DataFrame(r.json()[1])


url = 'http://api.worldbank.org/v2/countries/CH/indicators/SP.POP.TOTL/?format=json&date=200'

r = requests.get(url)

pd.DataFrame(r.json()[1])

