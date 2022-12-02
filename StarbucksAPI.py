import requests
import json
import time
import calendar
import hashlib

class Starbucks:
    bearer_token = None

    def get(self,url):
        headers = {'Authorization':'Bearer ' + self.bearer_token,'Accept':'application/json'}
        r = requests.get(url, headers=headers)
        if r.status_code != 200: raise Exception('API ERROR: '+ r.text)
        return json.load(r.text)

    def post(self, url,payload):
        headers = {'Authorization':'Bearer'+ self.bearer_token, 'Accept': 'application/json', 'Content-Type': 'application/json; charset=UTF-8'}
        r = requests.post(url,payload,headers=headers)
        if r.status_code != 200: raise Exception('API ERROR: '+ r.text)
        return json.load(r.text)
    
    def __init__(self,username,password):
        print('Signing in ' + username + '\n')
        try:
            timestamp = str(calendar.timegm(time.gmtime()))
            m = hashlib.md5()
            line = 'WGGkwQxE22H9yyYnRkv8Fjuf'+'9vghnze7n5kab8yssfd8phm'+timestamp
            m.update(line.encode(encoding='UTF-8',errors='strict'))
            sig = m.hexdigest()
            url = 'https://openapi.starbucks.com/v1/oauth/token?sig=' + sig
            payload = {'grant_type':'password','client_secret':'9vghnze7n5kab8yssfd8phm','client_id:':'WGGkwQxE22H9yyYnRkv8Fjuf','username':username,'password':password}
            headers = {'x-api-key':'WGGkwQxE22H9yyYnRkv8Fjuf'}
            r = requests.post(url,payload,headers=headers)
            # self.bearer_token = json.loads(r.text)['access_token']
            print(r.status_code)
        except:
           if r.status_code != 200: raise Exception('API ERROR: '+ r.text)

    def print_nearby_stores(self, lat, long):
        url = 'https://openapi.starbucks.com/v1/stores/nearby?latlng='+lat+','+lon+'&limit=5&radius=0.5xopState=true&userSubMarket=US&serviceTime=true&locale=en-US'
        results = self.get(url)
        for store in results['stores']:
            print('Name: '+store['store']['name'])
            print('Store Number '+store['store']['storeNumber']+'\n')

