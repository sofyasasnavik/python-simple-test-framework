import requests
import logging
from typing import Dict
from src.api.base_client import BaseHttpClient
from utils.config_loader import config

logger = logging.getLogger(__name__)


class SwapiClient(BaseHttpClient):
    """API client for SWAPI (Star Wars API) - swapi.dev"""
    
    def __init__(self):
        super().__init__()
    
    # Films endpoints
    def get_all_films(self, headers: Dict = None) -> requests.Response:
        return self.get(f"{config.swapi_base_url}/films/", headers=headers)
    
    def get_film_by_id(self, film_id: int, headers: Dict = None) -> requests.Response:
        return self.get(f"{config.swapi_base_url}/films/{film_id}/", headers=headers)
    
    # Planets endpoints
    def get_all_planets(self, headers: Dict = None) -> requests.Response:
        return self.get(f"{config.swapi_base_url}/planets/", headers=headers)
    
    def get_planet_by_id(self, planet_id: int, headers: Dict = None) -> requests.Response:
        return self.get(f"{config.swapi_base_url}/planets/{planet_id}/", headers=headers)
    
    # other endpoints
