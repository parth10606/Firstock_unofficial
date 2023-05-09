class Firstock:
    def __init__(self):
        self.actid = None
        self.jKey = None
        self.ws_thread = None
        self.hearbeat_thread = None
        self.ws = None
        self.ws_connected = False
        self.stop_heartbeat = False
        self.feed_message_handler = None
        self.order_feed_message_handler = None
        self.depth_feed_message_handler = None
        self.error_message_handler = None
        self.websocket_close_handler = None
        self.webscoket_open_handler = None
        self.freeze_qty_data = {
            'NIFTY':1800,
            'FINNIFTY':1800,
            'BANKNIFTY':900
        }
           
    #authentication methods
    from ._authentication import login,logout
    
    #place order and related data methods
    from ._order_methods import place_order,cancel_order,modify_order,place_multiple_orders,convert_position,get_order_book,get_trade_book,get_position_book,get_holdings,get_limits,get_single_order_history,order_margin,basket_margin

    #weboscket methods
    from ._websocket import send_ws_message,on_close,on_error,on_message,on_open,start_websocket,stop_websocket,subscribe_token,unsubscribe_token,connect_ws,Heartbeat,subscribe_order_update,subscribe_depth,unsubscribe_order_update,unsubscribe_depth
    from ._websocket_ack import connection_ack,touchline_ack,orderfeed_ack,depth_ack
    from ._websocket_on_message import feed_handler,order_feed_handler,depth_feed_handler

    #extras
    from ._quotes import get_quote,get_quote_ltp,get_multi_quotes,get_multi_quotes_ltp
    from ._strategies import place_order_strategy
    from ._general_methods import get_user_details,search_scrips,get_security_info,get_option_chain,get_index_list,span_calculator,time_price_series,option_greek,get_bse_symbols,get_index_symbols,get_nfo_symbols,get_nse_symbols,set_freeze_quantity