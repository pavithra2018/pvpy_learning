import requests
class api_auto() :
    def __init__(self, home_url) :
        self.base_url = home_url

    def http_caller(self, call_tag, url_tag, payload=None) :
        hcaller_function = getattr(requests, call_tag)
        if payload is None :
            result = hcaller_function( url = self.base_url + url_tag)
        else :
            result = hcaller_function( url = self.base_url + url_tag, data = payload)
        print("response code is:", result.status_code)
        print(result.text)

if __name__ == '__main__' :
    api_auto_obj = api_auto('https://jsonplaceholder.typicode.com')
    api_auto_obj.http_caller('get', '/posts/100')

    payload = {"userId": 10,"title":"new title", "body" : "wife of bhaskar"}
    api_auto_obj.http_caller('post', '/posts', payload)

    payload = {"userId": 10, "id": 100, "title":"chandana", "body" : "wife of bhaskar"}
    api_auto_obj.http_caller('put', '/posts/100', payload)

    payload = {"body" : "wife of bhaskar"}
    api_auto_obj.http_caller('patch', '/posts/100', payload)

    api_auto_obj.http_caller('delete','/posts/100')

