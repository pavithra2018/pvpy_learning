import requests
class api_auto() :
    def __init__(self, home_url) :
        self.base_url = home_url

    def http_get(self, url_tag = None) :
        if url_tag is None :
            result = requests.get(self.base_url)
        else :
            result = requests.get(self.base_url + url_tag)
        print("response code is:", result.status_code)
        print(result.text)

    def http_delete(self, url_tag) :
        print("INFO :Delete method")
        result = requests.delete(self.base_url + url_tag)
        print("response code is:", result.status_code)
        print(result.text)
        print("End of delete method")

    def http_patch(self, url_tag, payload) :
        print("INFO:patch method")
        result = requests.patch(self.base_url + url_tag, payload)
        print("response code is:", result.status_code)
        print(result.text)
        print("End of patch method")

    def http_put(self, url_tag, payload) :
        print("INFO:put method")
        result = requests.put(self.base_url + url_tag, payload)
        print("response code is:", result.status_code)
        print(result.text)
        print("End of put method")

    def http_post(self, url_tag, payload) :
        print("INFO: post method")
        result = requests.post(self.base_url + url_tag, payload)
        print("response code is:", result.status_code)
        print(result.text)
        print("End of post method")


if __name__ == '__main__' :
    api_auto_obj = api_auto('https://jsonplaceholder.typicode.com')
    
    api_auto_obj.http_get('/posts/100')

    payload = {"body" : "wife of bhaskar"}
    api_auto_obj.http_patch('/posts/100', payload)

    payload = {"userId": 10, "id": 100, "title":"chandana", "body" : "wife of bhaskar"}
    api_auto_obj.http_put('/posts/100', payload)

    payload = {"userId": 10,"title":"new title", "body" : "wife of bhaskar"}
    api_auto_obj.http_post('/posts', payload)

    api_auto_obj.http_delete('/posts/100')

























