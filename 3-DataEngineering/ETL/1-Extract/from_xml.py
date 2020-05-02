import pandas as pd
# Read a file line by line
def print_lines(n, file_name):
    f = open(file_name)
    for i in range(n):
        print(i, f.readline())
    f.close()

# import the BeautifulSoup library
from bs4 import BeautifulSoup

# open the population_data.xml file and load into Beautiful Soup
with open("population_data.xml") as fp:
    soup = BeautifulSoup(fp, "lxml") # lxml is the Parser type

# output the first 5 records in the xml file
# this is an example of how to navigate the XML document with BeautifulSoup

i = 0
# use the find_all method to get all record tags in the document
for record in soup.find_all('record'):
    # use the find_all method to get all fields in each record
    i += 1
    for record in record.find_all('field'):
        print(record['name'], ': ' , record.text)
    print()
    if i == 5:
        break


# Convert XML to df
i = 0
records = []
for record in soup.find_all('record'):
    fields = {}
    i += 1
    for record in record.find_all('field'):
        fields[record['name']] = record.text
    if i == 5:
        break
    records.append(fields)
print(records)  

df_xml = pd.DataFrame(records)
print(df_xml)

# Convert XML to df another way
data_dictionary = {'Country or Area':[], 'Year':[], 'Item':[], 'Value':[]}

for record in soup.find_all('record'):
    for record in record.find_all('field'):
        data_dictionary[record['name']].append(record.text)

df = pd.DataFrame.from_dict(data_dictionary)
df = df.pivot(index='Country or Area', columns='Year', values='Value')
df.reset_index(level=0, inplace=True)