from ._send_requests import send
from ._exception_handler import exception_handler,failure_response_handler

def place_order_strategy(self,data:dict,strategy_name:str)->list:
    data['userId']=self.actid,
    data['jKey']=self.jKey
    return send('POST',strategy_name,data)