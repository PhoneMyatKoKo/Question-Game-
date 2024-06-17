from typing import Any


class MyCustomMiddleware:
    def __init__(self,get_response) -> None:
        self.response=get_response
        
    def __call__(self,request, *args: Any, **kwds: Any) -> Any:
        print("My Middleware Working")
        request.kk="Customized request"
        
        
        response=self.response(request)
        
        print("Responding Custom Middleware.")
        request.ar="After view."
        
        
        
        return response