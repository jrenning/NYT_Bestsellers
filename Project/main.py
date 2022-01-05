import requests 
import config

# fucntions implemented to allow fro less repeatativeness
# also added for easier exploration of other parts of the API



# prints a list from the API based on the url json response and the certain section wanted
def print_response_list(response,response_keyword):
    for i,_ in enumerate(response['results']):
        print(f'{i+1}. {response1["results"][i][response_keyword]}') 


# makes a new list from the API based on the wnated response type 
def append_function(response,response_keyword):
    result = []
    for i,__ in enumerate(response['results']['books']):
        result.append(response['results']['books'][i][response_keyword])
    return result

# prints out a formatted list, optional argument of list2
def print_list(list1,list2=None):
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


title_result = append_function(response2,'title')

# print(f'The New York Times {response1["results"]["list_name_encoded"][list_type]} Bestseller List for {response2["last_modified"][:10]}')
print_list(title_result)

description_result = append_function(response2,'description')

print_list(description_result)

print_list(description_result,title_result)