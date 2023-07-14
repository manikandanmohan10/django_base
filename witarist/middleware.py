from typing import Any


class CustomMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        print('request')
        
        response = self.get_response(request)
    
        print('response')

        return response