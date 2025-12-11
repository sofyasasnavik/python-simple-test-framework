import os
from pathlib import Path
from typing import Any
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration class with typed properties"""
    swapi_base_url: str
    api_timeout: int
    retry_max_attempts: int
    retry_delay: float
    retry_backoff_factor: float
    log_level: str
    
    @classmethod
    def from_env(cls, env_file: str = ".env") -> "Config":
        """Create Config instance from environment variables"""
        load_dotenv(Path(env_file))
        
        return cls(
            swapi_base_url=os.getenv('SWAPI_BASE_URL', 'https://swapi.dev/api'),
            api_timeout=int(os.getenv('API_TIMEOUT', '30')),
            retry_max_attempts=int(os.getenv('RETRY_MAX_ATTEMPTS', '3')),
            retry_delay=float(os.getenv('RETRY_DELAY', '1.0')),
            retry_backoff_factor=float(os.getenv('RETRY_BACKOFF_FACTOR', '2.0')),
            log_level=os.getenv('LOG_LEVEL', 'INFO')
        )
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by attribute name"""
        return getattr(self, key, default)


config = Config.from_env()
