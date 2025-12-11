from faker import Faker
from typing import Dict, List, Any
import random
import string
import base64
import uuid
from datetime import datetime, timedelta


class DataGenerator:    
    def __init__(self, locale: str = 'en_US'):
        self.faker = Faker(locale)
        Faker.seed(random.randint(0, 10000))

    # generate random typed data
    def generate_random_string(self, length: int = 10) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def generate_random_number(self, min_val: int = 1, max_val: int = 100) -> int:
        return random.randint(min_val, max_val)

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    # generate random user related data
    def generate_user(self) -> Dict:
        return {
            "name": self.faker.name(),
            "email": self.faker.email(),
            "username": self.faker.user_name(),
            "phone": self.faker.phone_number(),
            "address": {
                "street": self.faker.street_address(),
                "city": self.faker.city(),
                "state": self.faker.state(),
                "zipcode": self.faker.zipcode(),
                "country": self.faker.country()
            },
            "company": self.faker.company(),
            "website": self.faker.url()
        }
    
    def generate_email(self, domain: str = None) -> str:
        if domain:
            return self.faker.email().split('@')[0] + '@' + domain
        return self.faker.email()
    
    def generate_phone(self) -> str:
        return self.faker.phone_number()
    
    def generate_phone_number(self) -> str:
        return self.faker.phone_number()

    def generate_address(self) -> Dict[str, str]:
        return {
            "street_address": self.faker.street_address(),
            "street_name": self.faker.street_name(),
            "building_number": self.faker.building_number(),
            "city": self.faker.city(),
            "state": self.faker.state(),
            "state_abbr": self.faker.state_abbr(),
            "zipcode": self.faker.zipcode(),
            "country": self.faker.country(),
            "country_code": self.faker.country_code(),
            "postcode": self.faker.postcode()
        }
    
    def generate_username(self) -> str:
        return self.faker.user_name()
    
    def generate_password(self, length: int = 12, special_chars: bool = True, 
                         digits: bool = True, upper_case: bool = True, 
                         lower_case: bool = True) -> str:
        return self.faker.password(
            length=length,
            special_chars=special_chars,
            digits=digits,
            upper_case=upper_case,
            lower_case=lower_case
        )