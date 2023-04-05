def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Unexpected Error occured\nFunction Name:{func.__name__}\nError:{e}")
    return inner_function


def failure_response_handler(error_name:str,res:dict)->bool:
    print(f'{error_name} Failed\nError Code: {res["code"]}\nError Name: {res["name"]}\nError Field: {res["error"]["field"]}\nError Message: {res["error"]["message"]}')
    return False