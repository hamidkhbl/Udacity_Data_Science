# ETL stands for Extract, Transform, Load.

# Extracting:

# Read CSV:

# Usefull codes:
df_projects.isnull().sum()  # Number of null values for each column
df_population.isnull().sum(axis=1)  # Number of null values for each row

df_population[df_population.isnull().any(axis=1)]  # rows having null values

# Null valur percentage per column
df_projects.isnull().sum() / df_projects.shape[0]

df_projects = pd.read_csv('projects_data.csv', dtype=str)

df_population = pd.read_csv('population_data.csv',
                            skiprows=4)  # skip 4 first rows


Read JSON:

df_json = pd.read_json('population_data.json', orient='records')

  # orient:
  #     'split': dict like {index -> [index], columns -> [columns], data -> [values]}
  #     'records': list like[{column -> value}, ..., {column -> value}]
  #     'index': dict like {index -> {column -> value}}
  #     'columns': dict like {column -> {index -> value}}
  #     'values': just the values array

# Read XML:

  # import the BeautifulSoup library
  from bs4 import BeautifulSoup

   # open the population_data.xml file and load into Beautiful Soup
   with open("population_data.xml") as fp:
        soup = BeautifulSoup(fp, "lxml")  # lxml is the Parser type

    # output the first 5 records in the xml file
    # this is an example of how to navigate the XML document with BeautifulSoup

    i = 0
    # use the find_all method to get all record tags in the document
    for record in soup.find_all('record'):
        # use the find_all method to get all fields in each record
        i += 1
        for record in record.find_all('field'):
            print(record['name'], ': ', record.text)
        print()
        if i == 5:
            break

# Convert XML to DataFrame
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
df_xml
