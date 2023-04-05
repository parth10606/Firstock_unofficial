from enum import Enum


class MessageTopic(str, Enum):
    """
    The message topic for each websocket message
    """
    CONNECTION = 'c'
    CONNECTION_ACK = 'ck'
    # SUBSCRIBE
    TOUCHLINE_FEED = 't'
    ACKNOWLEDGEMENT_FEED = 'tk'
    SUBSCRIBE_FEED = 'tf'
    UNSUBSCRIBE_FEED = 'u'
    SUBSCRIBE_UNSUB_ACK = 'uk'
    # DEPTH
    DEPTH_SUB = 'd'
    DEPTH_SUB_ACK = 'dk'
    DEPTH_FEED = 'df'
    DEPTH_UNSUB = 'ud'
    DEPTH_UNSUB_ACK = 'udk'
    # ORDER
    ORDER_SUB = 'o'
    ORDER_SUB_ACK = 'ok'
    ORDER_FEED = 'om'
    ORDER_UNSUB = 'uo'
    ORDER_UNSUB_ACK = 'uok'

    
