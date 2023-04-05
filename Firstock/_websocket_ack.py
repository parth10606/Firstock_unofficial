def connection_ack(self,message):
    if message['s']=='OK':
        print(f'Connection Successfull. Actid:{message["uid"]}')
    else:
        print('Connection Failed')

def touchline_ack(self,message):
    print(f'Subscribed...Exchange:{message["e"]} Token:{message["tk"]}')

def orderfeed_ack(self,message):
    print('Order Feed Subscribed')

def depth_ack(self,message):
    print(f'Subscribed...Exchange:{message["e"]} Token:{message["tk"]}')