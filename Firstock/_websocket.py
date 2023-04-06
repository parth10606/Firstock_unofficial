import json 
import websocket
import threading
import time 
from ._websocket_enums import MessageTopic
from ._logger import log

def send_ws_message(self,payload):
    self.ws.send(payload)

def on_message(self,ws, message):
    data = json.loads(message)
    if data['t']==MessageTopic.CONNECTION_ACK:
        self.connection_ack(data)
    elif data['t']==MessageTopic.ACKNOWLEDGEMENT_FEED:
        self.touchline_ack(data)
    elif data['t']==MessageTopic.ORDER_SUB_ACK:
        self.orderfeed_ack(data)
    elif data['t']==MessageTopic.DEPTH_SUB_ACK:
        self.depth_ack(data)

    elif data['t']==MessageTopic.SUBSCRIBE_FEED:
        self.feed_handler(data)

    elif data['t']==MessageTopic.ORDER_FEED:
        self.order_feed_handler(data)

    elif data['t']==MessageTopic.DEPTH_FEED:
        self.depth_feed_handler(data)


def on_error(self,ws, error):
    log.info(error)
    

def on_close(self,ws, close_status_code, close_msg):
    log.info("##Websocket Closed##")
    
    if self.websocket_close_handler !=None:
        self.websocket_close_handler(close_msg)

def on_open(self,ws):
    log.info("##Opened websocket connection##")
    self.connect_ws()
    if self.websocket_open_handler !=None:
        self.websocket_open_handler()

def connect_ws(self):
    values = {
        "t": MessageTopic.CONNECTION,
        "uid": self.actid,
        "actid":self.actid,
        "susertoken": self.jKey,
        "source": "API",
    }
    self.send_ws_message(json.dumps(values))
    

def Heartbeat(self):
    global exception
    exception=False
    while not self.stop_heartbeat:
        try:
            self.connect_ws()
            time.sleep(30)
        except Exception as e:
            log.info('Exception Occured in Heartbeat')
            log.info(e)
            exception=True
            break
    
    if exception:
        log.info('Stoping Websocket')
        self.stop_websocket(True)



def start_websocket(self,websocket_open_handler=None,websocket_close_handler=None,feed_message_handler=None,error_message_handler=None,order_feed_message_handler=None,depth_feed_message_handler=None):
    self.websocket_open_handler = websocket_open_handler
    self.websocket_close_handler=websocket_close_handler
    self.feed_message_handler=feed_message_handler
    self.error_message_handler=error_message_handler
    self.order_feed_message_handler =order_feed_message_handler
    self.depth_feed_message_handler = depth_feed_message_handler

    self.ws = websocket.WebSocketApp("wss://norenapi.thefirstock.com/NorenWSTP/",
                                on_open=self.on_open,
                                on_message=self.on_message,
                                on_error=self.on_error,
                                on_close=self.on_close)

    self.ws_thread= threading.Thread(target=self.ws.run_forever) 
    self.heartbeat_thread = threading.Thread(target=self.Heartbeat)
    self.heartbeat_thread.daemon = True
    self.ws_thread.daemon = True
    self.stop_heartbeat = False
    self.ws_thread.start()
    time.sleep(2)
    self.heartbeat_thread.start()


def stop_websocket(self,exception=False):
    self.stop_heartbeat = True
    time.sleep(1)
    self.heartbeat_thread.join()
    if not exception:
        self.ws.close()     
    self.ws_thread.join()
    if exception:
        log.info('Restarting Websocket...')
        self.start_websocket(websocket_open_handler=self.websocket_open_handler,websocket_close_handler=self.websocket_close_handler,feed_message_handler=self.feed_message_handler,error_message_handler=self.error_message_handler,order_feed_message_handler=self.order_feed_message_handler,depth_feed_message_handler=self.depth_feed_message_handler)
    

def subscribe_token(self,data:list):
    l = [f"{i['exchange']}|{i['token']}" for i in data]
    s = "#".join(l)
    val = {
        "t":MessageTopic.TOUCHLINE_FEED,
        "k":s
    }
    self.send_ws_message(json.dumps(val))

def unsubscribe_token(self,data:list):
    l = [f"{i['exchange']}|{i['token']}" for i in data]
    s = "#".join(l)
    val = {
        "t":MessageTopic.UNSUBSCRIBE_FEED,
        "k":s
    }
    self.send_ws_message(json.dumps(val))

def subscribe_order_update(self):
    val = {
        "t":MessageTopic.ORDER_SUB,
        "actid":self.actid
    }
    self.send_ws_message(json.dumps(val))

def unsubscribe_order_update(self):
    val = {
        "t":MessageTopic.ORDER_UNSUB,
    }
    self.send_ws_message(json.dumps(val))

def subscribe_depth(self,data:list):
    l = [f"{i['exchange']}|{i['token']}" for i in data]
    s = "#".join(l)
    val = {
        "t":MessageTopic.DEPTH_SUB,
        "k":s
    }
    self.send_ws_message(json.dumps(val))

def unsubscribe_depth(self,data:list):
    l = [f"{i['exchange']}|{i['token']}" for i in data]
    s = "#".join(l)
    val = {
        "t":MessageTopic.DEPTH_UNSUB,
        "k":s
    }
    self.send_ws_message(json.dumps(val))