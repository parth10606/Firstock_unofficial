import requests
from ._end_points import end_points
from ._exception_handler import exception_handler

@exception_handler
def send(method:str, url:str, payload=None)->dict:
    if method=='POST':
        res = requests.post(end_points[url],json=payload)
        return res.json()