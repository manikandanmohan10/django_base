import logging
from typing import Any
from .utils import get_log_string
logger = logging.getLogger(__name__)

class CustomMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request) -> Any:
        print('request')
        
        response = self.get_response(request)
    
        print('response')
        # logger.info('-----------INFO------------------')
        # logger.debug('-----------DEBUG------------------')
        logger.error(get_log_string(request))
        return response