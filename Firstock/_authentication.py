from ._exception_handler import exception_handler,failure_response_handler
from ._send_requests import send

@exception_handler
def login(self,user_id='',password='',totp='',vender_code='',api_key='')->bool:
    """
    Firstock Login 
    """
    payload = {
        "userId": user_id,
        "password": password,
        "TOTP": totp,
        "vendorCode": vender_code,
        "apiKey": api_key   
    }
    res= send('POST','login',payload)

    if res['status'] != 'Success':
        return failure_response_handler('Login',res)
    
    self.jKey = res['data']['susertoken']
    self.actid = res['data']['actid']
    return True
    


@exception_handler
def logout(self)->bool:
    """
    Firstock Logout
    """
    payload = {
        'jKey':self.jKey,
        'userId':self.actid
    }
    res= send('POST','logout',payload)

    if res['status'] != 'Success':
        return failure_response_handler('Logout',res)
    
    self.jKey = ''
    return True
