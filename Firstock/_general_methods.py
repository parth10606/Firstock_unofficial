from ._send_requests import send
from ._exception_handler import exception_handler,failure_response_handler


@exception_handler
def get_user_details(self)->dict:
    """
    Return user details of logged in user
    """
    payload = {
        'jKey':self.jKey,
        'userId':self.actid
    }
    res= send('POST','user_details',payload)

    if res['status'] != 'Success':
        return failure_response_handler('Fetching Userdetails',res)
    
    return res['data']

@exception_handler
def search_scrips(self,stext:str)->list:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'stext':stext
    }

    res = send('POST','search_scrips',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Search Scrips',res)
    return res['values']

@exception_handler
def get_security_info(self,exchange='',token='')->dict:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'exchange':exchange,
        'token':token
    }

    res = send('POST','get_security_info',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Security Info',res)
    return res['data']

@exception_handler
def get_index_list(self,exchange='')->list:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'exchange':exchange
    }

    res = send('POST','get_index_list',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Index list',res)
    return res['data']['values']

@exception_handler
def get_option_chain(self,exchange='',tradingSymbol='',strikePrice='',count='')->list:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'exchange':exchange,
        'tradingSymbol':tradingSymbol,
        'strikePrice':strikePrice,
        'count':count
    }

    res = send('POST','get_option_chain',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Option chain',res)
    return res['data']['values']

@exception_handler
def span_calculator(self,data:list)->dict:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'data':data
    }
    res = send('POST','span_calculator',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Span Calculator',res)
    return res['data']

@exception_handler
def time_price_series(self,exchange='',token='',startTime='',endTime='',interval='')->list:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'exchange':exchange,
        'token':token,
        'startTime':startTime,
        'endTime':endTime,
        'interval':interval
    }

    res = send('POST','time_price_series',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Time price series',res)
    return res['data']

@exception_handler
def option_greek(self,expiryDate='',strikePrice='',spotPrice='',initRate='',volatility='',optionType='')->dict:
    payload = {
        'jKey':self.jKey,
        'userId':self.actid,
        'expiryDate':expiryDate,
        'strikePrice':strikePrice,
        'spotPrice':spotPrice,
        'initRate':initRate,
        'volatility':volatility,
        'optionType':optionType    
    }

    res = send('POST','option_greek',payload)
    if res['status'] != 'Success':
        return failure_response_handler('Option greek',res)
    return res['data']



