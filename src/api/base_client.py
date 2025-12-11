import requests
import logging
from typing import Dict, Any, Optional
from utils.config_loader import config

logger = logging.getLogger(__name__)


class BaseHttpClient:    
    def __init__(self, timeout: int = None):
        self.timeout = timeout or config.api_timeout
        self.session = requests.Session()
    
    def get(self, url: str, params: Dict = None, headers: Dict = None) -> requests.Response:
        logger.info(f"GET request to: {url}")
        response = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def post(self, url: str, data: Any = None, json: Dict = None, 
             headers: Dict = None, files: Dict = None) -> requests.Response:
        logger.info(f"POST request to: {url}")
        response = self.session.post(
            url, data=data, json=json, headers=headers, 
            files=files, timeout=self.timeout
        )
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def put(self, url: str, data: Any = None, json: Dict = None, 
            headers: Dict = None) -> requests.Response:
        logger.info(f"PUT request to: {url}")
        response = self.session.put(url, data=data, json=json, headers=headers, timeout=self.timeout)
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def patch(self, url: str, data: Any = None, json: Dict = None, 
              headers: Dict = None) -> requests.Response:
        logger.info(f"PATCH request to: {url}")
        response = self.session.patch(url, data=data, json=json, headers=headers, timeout=self.timeout)
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def delete(self, url: str, headers: Dict = None) -> requests.Response:
        logger.info(f"DELETE request to: {url}")
        response = self.session.delete(url, headers=headers, timeout=self.timeout)
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def close(self):
        self.session.close()
