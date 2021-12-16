import requests 
import config
import json

# prints out lits of all of the NYT bestseller lists 
url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={config.API_KEY}'
response1 = requests.get(url).json()

for i in range(len(response1['results'])):
    print(f'{i+1}. {response1["results"][i]["list_name_encoded"]}')
    
# url to the nyt API
list_type = int(input('Input the desired NYT bestseller list')) or 3

url2 = f'https://api.nytimes.com/svc/books/v3/lists/current/{response1["results"][list_type]["list_name_encoded"]}.json?api-key={config.API_KEY}'

# request API data and sort the json data 
response2 = requests.get(url2).json()

title_result = []

for i in range(len(response2['results']['books'])):
    title_result.append(response2['results']['books'][i]['title'])
    
print(f'The New York Times {response1["results"][i]["list_name_encoded"]} Bestseller List for {response2["last_modified"][:10]}')
for i in range(len(title_result)):
    print(f'{i+1}. {title_result[i]}')
    

# makes a list of all of the bestseller descriptions
description_result = []

for i in range(len(response2['results']['books'])):
    description_result.append(response2['results']['books'][i]['description'])

# prints out descriptions
for i in range(len(description_result)):
    print(f'{i+1}. {description_result[i]}')

# combined title and description output 
for i in range(len(description_result)):
    print(f'{i+1}. {title_result[i]}: {description_result[i]}')