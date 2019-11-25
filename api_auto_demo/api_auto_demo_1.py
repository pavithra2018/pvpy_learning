import requests

result = requests.get('https://jsonplaceholder.typicode.com/posts/100')        
print(type(result))
print("response code is:", result.status_code)
print(result.text)

result = requests.delete('https://jsonplaceholder.typicode.com/posts/100')
print(type(result))
print("response code is:", result.status_code)
print(result.text)

'''
{
  "userId": 10,
  "id": 100,
  "title": "at nam consequatur ea labore ea harum",
  "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
}
'''

payload = { 'body' : "wife of bhaskar" }
result = requests.patch(url = 'https://jsonplaceholder.typicode.com/posts/100', data = payload)
print(type(result))
print("response code is:", result.status_code)
print(result.text)

payload = {"userId": 10,"id": 100,"title":"new title", "body" : "wife of bhaskar" }
result = requests.put(url = 'https://jsonplaceholder.typicode.com/posts/100', data = payload)
print(type(result))
print("response code is:", result.status_code)
print(result.text)

payload = {"userId": 10,"title":"new title", "body" : "wife of bhaskar" }
result = requests.post(url = 'https://jsonplaceholder.typicode.com/posts', data = payload)
print(type(result))
print("response code is:", result.status_code)
print(result.text)




