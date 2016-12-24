from bs4 import BeautifulSoup
import requests
import pandas as pd

# HTML to BeautifulSoup
url = "https://www.directathletics.com/results/xc/10807.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

# Finding table and table data
mens_table = soup.find_all('table')[3]
mens_rows = table.find_all('tr')[1:]

womens_table = soup.find_all('table')[5]
womens_rows = table.find_all('tr')[1:]

# Creating dictionaries
variables = ['place', 'name', 'year', 'team', 'avg mile', 'time', 'score']

mens = {}
womens = {}

dictionaries = [mens, womens]

for variable in variables:
    mens[variable] = []
    womens[variable] = []

def assigning_values(dictionary, row_list):
	for row in row_list:
	    cols = row.find_all('td')
	    dictionary['place'].append(cols[0].get_text())
	    dictionary['name'].append(cols[1].get_text())
	    dictionary['year'].append(cols[2].get_text())
	    dictionary['team'].append(cols[3].get_text())
	    dictionary['avg mile'].append(cols[4].get_text())
	    dictionary['time'].append(cols[5].get_text())
	    dictionary['score'].append(cols[6].get_text())

assigning_values(mens, mens_rows)
assigning_values(womens, womens_rows)

# Cleaning and writing to CSV
for key in mens:
    mens[key] = [x.strip('\n') for x in mens[key]]

for key in womens:
    womens[key] = [x.strip('\n') for x in womens[key]]

mens_data = pd.DataFrame(mens)
mens_data.to_csv("Mens.csv")

womens_data = pd.DataFrame(womens)
womens_data.to_csv("Womens.csv")