from ._send_requests import send
from ._exception_handler import exception_handler,failure_response_handler
from ._end_points import download_bse_eq_symbols,download_index_symbols,download_nfo_symbols,download_nse_eq_symbols

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



@exception_handler
def get_nfo_symbols(self):
    print('Fetching NFO Data....')
    res=send('GET',download_nfo_symbols)
    with open('NFO_Symbols.csv','w') as f:
        f.write(res.text)
    print('Data received')

@exception_handler
def get_nse_symbols(self):
    print('Fetching NSE Data....')
    res=send('GET',download_nse_eq_symbols)
    with open('NSE_Symbols.csv','w') as f:
        f.write(res.text)
    print('Data received')

@exception_handler
def get_bse_symbols(self):
    print('Fetching BSE Data....')
    res=send('GET',download_bse_eq_symbols)
    with open('BSE_Symbols.csv','w') as f:
        f.write(res.text)
    print('Data received')

@exception_handler
def get_index_symbols(self):
    print('Fetching Index Data....')
    res=send('GET',download_index_symbols)
    with open('Index_Symbols.csv','w') as f:
        f.write(res.text)
    print('Data received')

@exception_handler
def set_freeze_quantity(self, freeze_qty_obj=None):
    """
    To set freeze quantity 
    Please provide your desired quantity
    if you set freeze quantity for NIFTY as 500 and you place order for 1000 qty, two orders of 500 will be set to broker from place_order

    NOTE: if freeze quantity is not set, It is by default the NSE freeze quantity. ONLY NIFTY, BANKNIFTY and FINNIFTY are set here by default.
    To set freeze qunatity for other Derivates you need to refer to freeze quantity xls doc from NSE and set it here by passing object.
    
    """
    if freeze_qty_obj is None:
        return False
    for key in freeze_qty_obj:
        self.freeze_qty_data[key]=freeze_qty_obj[key]
    return True