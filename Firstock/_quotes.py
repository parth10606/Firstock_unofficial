from ._send_requests import send
from ._exception_handler import exception_handler,failure_response_handler

@exception_handler
def get_quote(self,exchange='',token='')->dict:
    payload = {
        "userId": self.actid,
        "jKey": self.jKey,
        "exchange": exchange,
        "token": token
    }
    res = send('POST','get_quote',payload)
    if res['status']!='Success':
        return failure_response_handler('Get Quote',res)
    return res['data']

@exception_handler
def get_quote_ltp(self,exchange='',token='')->dict:
    payload = {
        "userId": self.actid,
        "jKey": self.jKey,
        "exchange": exchange,
        "token": token
    }
    res = send('POST','get_quote_ltp',payload)
    if res['status']!='Success':
        return failure_response_handler('Get Quote Ltp',res)
    return res['data']

@exception_handler
def get_multi_quotes(self,data:list)->list:
    payload = {
        "userId": self.actid,
        "jKey": self.jKey,
        "data":data
    }
    res = send('POST','get_multi_quotes',payload)
    if res['status']!='Success':
        return failure_response_handler('Get MultiQuotes',res)
    return res['data']

@exception_handler
def get_multi_quotes_ltp(self,data:list)->list:
    payload = {
        "userId": self.actid,
        "jKey": self.jKey,
        "data":data
    }
    res = send('POST','get_multi_quotes_ltp',payload)
    if res['status']!='Success':
        return failure_response_handler('Get MultiQuotes Ltp',res)
    return res['data']