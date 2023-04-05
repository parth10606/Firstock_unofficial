from ._exception_handler import exception_handler,failure_response_handler
from ._send_requests import send


#Place Order Functions
@exception_handler
def place_order(self,exchange='',symbol='',qty='',transaction_type='',product='',price='',trigger_price='',price_type='',remark="Parth's Firstock Module",retention='DAY')->str:
    payload = {
        "userId": self.actid,
        "exchange": exchange,
        "tradingSymbol": symbol,
        "quantity": str(qty),
        "price": price,
        "product": product,
        "transactionType": transaction_type,
        "priceType": price_type,
        "retention": retention,
        "triggerPrice": trigger_price,
        "remarks": remark,
        "jKey":self.jKey,
    }
    res = send('POST','place_order',payload)
    if res['status']!='Success':
        return failure_response_handler('Place Order',res)
    return res['data']['orderNumber']

@exception_handler
def cancel_order(self,order_number:str)->str:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
        "orderNumber":order_number
    }
    res = send('POST','cancel_order',payload)
    if res['status']!='Success':
        return failure_response_handler('Cancel order',res)
    return res['data']['orderNumber']

@exception_handler
def modify_order(self,order_number="",quantity="",price="",triggerPrice="",exchange="",tradingSymbol="",priceType="")->str:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
        "orderNumber":order_number,
        "quantity":quantity,
        "price":price,
        "triggerPrice":triggerPrice,
        "exchange":exchange,
        "tradingSymbol":tradingSymbol,
        "priceType":priceType
    }
    res = send('POST','modify_order',payload)
    if res['status']!='Success':
        return failure_response_handler('Modify order',res)
    return res['data']['orderNumber']

@exception_handler
def place_multiple_orders(self,data:list)->list:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
        "data":data
    }
    return send('POST','multi_place_order',payload)

@exception_handler
def convert_position(self,data:dict)->dict:
    data['userId']=self.actid
    data['jKey']=self.jKey
    return send('POST','product_conversion',data)



#Get Data Functions
@exception_handler
def get_order_book(self)->list:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
    }
    res = send('POST','order_book',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching order book',res)
    return res['data']


@exception_handler
def get_trade_book(self)->list:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
    }
    res = send('POST','trade_book',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching trade book',res)
    return res['data']

@exception_handler
def get_position_book(self)->list:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
    }
    res = send('POST','position_book',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching position book',res)
    return res['data']

@exception_handler
def get_holdings(self)->list:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
    }
    res = send('POST','holdings',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching holdings',res)
    return res['data']

@exception_handler
def get_limits(self)->dict:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
    }
    res = send('POST','limit',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching limits',res)
    return res['data']


@exception_handler
def get_single_order_history(self,order_number:str)->dict:
    payload = {
        "userId":self.actid,
        "jKey":self.jKey,
        "orderNumber":order_number
    }
    res = send('POST','single_order_history',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetching Order history',res)
    return res['data'][0]



#Get Margin Functions
@exception_handler
def order_margin(self,exchange='',symbol='',qty='',transaction_type='',product='',price='',price_type='')->dict:
    payload = {
        "userId": self.actid,
        "exchange": exchange,
        "tradingSymbol": symbol,
        "quantity": str(qty),
        "price": price,
        "product": product,
        "transactionType": transaction_type,
        "priceType": price_type,
        "jKey":self.jKey,
    }
    res = send('POST','order_margin',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetch order margin',res)
    return res['data']

def basket_margin(self,data:list)->dict:
    payload = {
        "userId": self.actid,
        "jKey":self.jKey,
        "basket":data
    }
    res = send('POST','basket_margin',payload)
    if res['status']!='Success':
        return failure_response_handler('Fetch order margin',res)
    return res['data']