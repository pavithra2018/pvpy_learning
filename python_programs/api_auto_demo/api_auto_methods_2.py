import requests

# get is used to read the data from server
def get(g_url,  eid=None):
    if eid is None :
        result = requests.get(g_url)
    else :
        result = requests.get(g_url+'/%s'%eid)
    print(type(result))
    print("response code is:", result.status_code)
    print(result.text)
    
# delete is used to delete the data from database    
def delete(d_url):
    print("INFO: http delete on %s"%d_url)
    result = requests.get(d_url)
    print(type(result))
    print("response code is:", result.status_code)
    print(result.text)
    print("End of delete method") 
'''
{
  "userId": 10,
  "id": 100,
  "title": "at nam consequatur ea labore ea harum",
  "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
}
'''
# patch is used to update or modify the data
def patch(pa_url, pa_data):
   result = requests.patch(pa_url, pa_data)  
   print(type(result))
   print("response code is:", result.status_code)
   print(result.text)
   
# put is used to update or replace the data   
def put(pu_url, pu_data): 
    result = requests.put(pu_url , pu_data)
    print(type(result))
    print("response code is:", result.status_code)
    print(result.text)

# post is used to create a new record    
def post(po_url, po_data):
    result = requests.post(po_url, po_data)
    print(type(result))
    print("response code is:", result.status_code)
    print(result.text)


if __name__ == '__main__' :
    home_url = 'https://jsonplaceholder.typicode.com'
    # get(home_url+'/posts')
    print("data for id 100")
    get(home_url+'/posts',100)
   
    print("INFO: Doing post() now")
    po_data = {"userId": 10,"title":"new title", "body" : "wife of bhaskar"}
    post( home_url+'/posts', po_data)

    print("INFO: Doing put() now")
    pu_data = {"userId": 10, "id": 100, "title":"chandana", "body" : "wife of bhaskar"}
    put( home_url+'/posts/100', pu_data)

    print("INFO: Doing patch() now")
    pa_data = {"body" : "wife of bhaskar"}
    patch( home_url + '/posts/100', pa_data)

    print('%' * 75)
    get(home_url+'/posts',100)
    delete(home_url+'/posts/100')
    get(home_url+'/posts',100)




