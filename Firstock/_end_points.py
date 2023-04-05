root = 'https://connect.thefirstock.com/api/V3/'
ws_endpoint = 'wss://norenapi.thefirstock.com/NorenWSTP'

end_points={
    'login' :f'{root}login',
    'logout' : f'{root}logout',
    'user_details' : f'{root}userDetails',

    'place_order':f'{root}placeOrder',
    'multi_place_order':f'{root}multiPlaceOrders',
    'order_margin':f'{root}orderMargin',
    'order_book':f'{root}orderBook',
    'cancel_order':f'{root}cancelOrder',
    'modify_order':f'{root}modifyOrder',
    'single_order_history':f'{root}singleOrderHistory',
    'trade_book':f'{root}tradeBook',
    'position_book':f'{root}positionBook',
    'product_conversion':f'{root}productConversion',
    'holdings':f'{root}holdings',
    'limit':f'{root}limit',
    'basket_margin':f'{root}basketMargin',

    'get_quote':f'{root}getQuote',
    'get_quote_ltp':f'{root}getQuote/ltp',
    'get_multi_quotes':f'{root}getMultiQuotes',
    'get_multi_quotes_ltp':f'{root}getMultiQuotes/ltp',
    'search_scrips':f'{root}searchScrips',
    'get_security_info':f'{root}securityInfo',
    'get_index_list':f'{root}indexList',
    'get_option_chain':f'{root}optionChain',
    'span_calculator':f'{root}spanCalculators',
    'time_price_series':f'{root}timePriceSeries',
    'option_greek':f'{root}optionGreek',

    'bear_put_spread':f'{root}strategies/bearPutSpread',
    'bull_call_spread':f'{root}strategies/bullCallSpread',
    'long_strangle':f'{root}strategies/longStrangle',
    'long_straddle':f'{root}strategies/longStraddle',
    'short_straddle':f'{root}strategies/shortStraddle',
    'short_strangle':f'{root}strategies/shortStrangle',
}
