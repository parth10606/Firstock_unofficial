from ._logger import log

def connection_ack(self,message):
    if message['s']=='OK':
        print('Connection Successfull...')
    else:
        print('Connection Failed')

def touchline_ack(self,message):
    print(f'Subscribed to - Exchange:{message["e"]} Token:{message["tk"]}')

def orderfeed_ack(self,message):
    print('Order Feed Subscribed')

def depth_ack(self,message):
    print(f'Subscribed to - Exchange:{message["e"]} Token:{message["tk"]}')