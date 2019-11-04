import json
import requests
import pandas
from pandas.io.json import json_normalize

# Define the initial API endpoint URL
url = 'https://rickandmortyapi.com/api/character/?page=1'

response = requests.get(url)
results = response.json()
#list_chars = [] # En lista funciona pero queda dentro de otra lista y dificulta su mutacion


def all_chars():
    list_chars = pandas.DataFrame()
    for i in range(16):
        url = 'https://rickandmortyapi.com/api/character/?page='
        if i == 0:
            continue
        elif i >= 1:
            new_url = str(url)+str(i)  # crea el url
            new_request = requests.get(new_url)  # hace el request
            new_result = new_request.json()  # devuelve el JSON
            data = pandas.DataFrame(new_result['results'])
            list_chars = list_chars.append(data)
    list_chars.to_csv('chars.csv', index=False)
    return list_chars

print(all_chars())