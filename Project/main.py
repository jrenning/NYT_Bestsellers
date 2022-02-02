import requests 
import config


def print_response_list(response,response_keyword):
    """
    prints a list from the API based on the url json response and the certain section wanted. 
    response = API response dictionaryr
    response_keyword = section of results wanted 
    """
    for i,_ in enumerate(response['results']):
        print(f'{i+1}. {response1["results"][i][response_keyword]}') 



def new_response_list(response,response_keyword):
    """
    makes a new list from the API based on the wanted response type 
    response = API response dictionaryr
    response_keyword = section of results wanted 
    """
    result = []
    for i,__ in enumerate(response['results']['books']):
        result.append(response['results']['books'][i][response_keyword])
    return result

def print_bulleted_list(list1,list2=None):
    """
    prints out a formatted list with numbered bullets. list2 is an optional argument
    """
    for i,_ in enumerate(list1):
        if list2 == None:
            print(f'{i+1}. {list1[i]}')
        else:
            print(f'{i+1}. {list2[i]}: {list1[i]}')



# prints out lits of all of the NYT bestseller lists 
url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={config.API_KEY}'
response1 = requests.get(url).json()

print_response_list(response1,'list_name_encoded')
    
# url to the nyt API
list_type = int(input('Input the desired NYT bestseller list: ')) or 3


url2 = f'https://api.nytimes.com/svc/books/v3/lists/current/{response1["results"][list_type]["list_name_encoded"]}.json?api-key={config.API_KEY}'
response2 = requests.get(url2).json()


title_result = new_response_list(response2,'title')

# print(f'The New York Times {response1["results"]["list_name_encoded"][list_type]} Bestseller List for {response2["last_modified"][:10]}')
print_bulleted_list(title_result)

description_result = new_response_list(response2,'description')

print_bulleted_list(description_result)

print_bulleted_list(description_result,title_result)
