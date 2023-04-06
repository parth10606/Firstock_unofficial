
# Firstock unoffical SDK 

This is a free to use non-official firstock python-sdk. 

Licensed under the MIT License.

## v0.0.1 - Features
* Stateless.
* Websockets exceptions handled.
* Logger for Firstock.
* Uses v3 connect firstock endpoints.
* Configure multiple users in same module.

## Usage
* Logging In and Logging Out
```python
from Firstock import Firstock

#Creating a firstock api object
api = Firstock()

#firstock login
api.login(user_id='<your firstock actid>',password='<firstock password>',totp='<OTP/TOTP>',vender_code='<your Vendor code>',api_key='<API key from firstock>')

#firstock logut
api.logout()

```
* Place Order
```python 
#After logging in you can use api object to place orders
order_number = api.place_order(
    exchange='', 
    symbol='',
    qty='',
    transaction_type='',
    product='',
    price='',
    trigger_price='',
    price_type='',
    retention='DAY',  
    remark='My Algo'
)
print(f'Order Placed: {order_number}')
order = api.get_single_order_history(order_number)
print(order)

#Cancel Order
c_order_number = api.cancel_order('<your order number>')
print(f'Order Cancelled: {c_order_number}')


#Modify Order
m_order_number = api.modify_order(
    order_number='',
    quantity='',
    price='',
    triggerPrice='',
    exchange='',
    tradingSymbol='',
    priceType=''
)
print(f'Order Modified: {m_order_number}')


#Place Multiple Orders (Basket Orders)
orderObj=[
    {
        "exchange": "NSE",
        "tradingSymbol": "ITC-EQ",
        "quantity": "1",
        "price": "0",
        "product": "I",
        "transactionType": "B",
        "priceType": "MKT",
        "retention": "DAY",
        "triggerPrice": "800",
        "remarks": "Test1"
    },
    {
        "exchange": "NSE",
        "tradingSymbol": "YESBANK-EQ",
        "quantity": "1",
        "price": "0",
        "product": "I",
        "transactionType": "B",
        "priceType": "MKT",
        "retention": "DAY",
        "triggerPrice": "800",
        "remarks": "Test1"
    }
]
order_number_list = api.place_multiple_orders(orderObj)
print(order_number_list)

```
* Quotes
```python
q = api.get_quote(exchange='',token='')
print(q)

#quote ltp
ql = api.get_quote_ltp(exchange='',token='')
print( ql)

#multi quotes
data =[
    {
        "exchange": "NSE",
        "token": "26000"
    },
    {
        "exchange": "NFO",
        "token": "55101"
    }
]

mq = api.get_multi_quotes(data)
print(mq)

#multi quotes ltp
mql = api.get_multi_quotes_ltp(data)
print(mql)

```
* General Methods 
```python 
print(api.get_user_details()) #gives you account details

print(api.search_scrips('ITC')) #search

print(api.get_security_info(exchange='',token='')) # info on given toekn

print(api.get_index_list(exchange='')) #list all indices

#Option Chain 
oc = api.get_option_chain(exchange='NFO',tradingSymbol='',strikePrice='',count='')

print(oc)

#Option Greek 
print(api.option_greek(
    expiryDate='',
    strikePrice='',
    spotPrice='',
    initRate='',
    volatility='',
    optionType=''
))

```
* Historical data
```python
timePriceSeries = api.time_price_series(
    exchange="NSE",
    token="22",
    startTime="16/08/2022 09:45:32",
    endTime="15/02/2023 13:45:32",
    interval="5"
)

```
* Strategies
```python 
data = {
   "symbol": "NIFTY",
   "putBuyStrikePrice": "18000",
   "putSellStrikePrice": "17800",
   "expiry": "23FEB23",
   "product": "C",
   "quantity": "10",
   "remarks": "My put spread",
}
order_number_list = api.place_order_strategy(data,'bear_put_spread')

```
* Websockets
```python

def my_order_feed_handler(message):
    #do something with message other than printing
    return True

def my_feed_handler(message):
    #do something other than printing
    return True

api.start_websocket(feed_message_handler=my_feed_handler,order_feed_message_handler=my_order_feed_handler)
# You can also provie other message handlers, hover on start_websocket to check more

api.subscirbe_token([{'exchange':'NSE','token':'26000'},{'exchange':'NFO','token':'44256'}])
#list of exchange and token dictionary is expected

api.subscirbe_order_update() #to get order updates via websocket
```
You can refer to official api documentation in Docs tab at

https://connect.thefirstock.com/

## Updates 
* Logger added