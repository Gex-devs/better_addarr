import requests
import json

class RadarrApi:
    def __init__(self, apiKey,host,port):
        self.apiKey = apiKey
        self.host = f"http://{host}:{port}"
        self.headers = {
            "accept":"application/json",
            "X-Api-Key":self.apiKey
        }


    def getApiversion(self):
        request = requests.get(self.host+"/api",headers=self.headers)
        if request.status_code == 200:    
            return json.loads(request.content)["current"]
        
    def lookup(self,title):
        request = requests.get(self.host+f"/api/{self.getApiversion()}/movie/lookup?term={title}",headers=self.headers)
        if request.status_code == 200:    
            jj = request.json()
            return jj
            



    
        
    


    


