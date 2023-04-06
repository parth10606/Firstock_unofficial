from ._logger import log

def connection_ack(self,message):
    if message['s']=='OK':
        log.info('Connection Successfull...')
    else:
        log.info('Connection Failed')

def touchline_ack(self,message):
    log.info(f'Subscribed to - Exchange:{message["e"]} Token:{message["tk"]}')

def orderfeed_ack(self,message):
    log.info('Order Feed Subscribed')

def depth_ack(self,message):
    log.info(f'Subscribed to - Exchange:{message["e"]} Token:{message["tk"]}')