import requests
from ._end_points import end_points
from ._exception_handler import exception_handler

@exception_handler
def send(method:str, url:str, payload=None)->dict:
    if method=='POST':
        res = requests.post(end_points[url],json=payload)
        if 'status' not in res.json():
            print(f'{url} failed for client {payload["userId"]}. No response from firstock')
            return {'status':'failed','code':400,'name':'No response','error':{'field':'none','message':'No response from Firstock'}}
        
        return res.json()
    
    if method=='GET':
        return requests.get(url)