import pytest
import logging
import time
from functools import wraps
from typing import Callable, Tuple, Type
from utils.config_loader import config

logger = logging.getLogger(__name__)


def retry_flaky_test(
    max_attempts: int = None,
    delay: float = None,
    backoff_factor: float = None,
    exceptions: Tuple[Type[Exception], ...] = (AssertionError, Exception)
):
    """
    Decorator to retry flaky tests.
    """
    max_attempts = max_attempts or config.retry_max_attempts
    delay = delay or config.retry_delay
    backoff_factor = backoff_factor or config.retry_backoff_factor
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.info(f"🔄 Test '{func.__name__}' - Attempt {attempt}/{max_attempts}")
                    result = func(*args, **kwargs)
                    
                    if attempt > 1:
                        logger.info(f"✅ Test '{func.__name__}' passed on attempt {attempt}")
                    
                    return result
                    
                except exceptions as e:
                    last_exception = e
                    
                    if attempt < max_attempts:
                        logger.warning(
                            f"⚠️  Test '{func.__name__}' failed on attempt {attempt}/{max_attempts}: {str(e)}"
                        )
                        logger.info(f"⏳ Waiting {current_delay:.1f}s before retry...")
                        time.sleep(current_delay)
                        current_delay *= backoff_factor
                    else:
                        logger.error(
                            f"❌ Test '{func.__name__}' failed after {max_attempts} attempts"
                        )
            
            # If we've exhausted all retries, raise the last exception
            raise last_exception
        
        return wrapper
    return decorator
