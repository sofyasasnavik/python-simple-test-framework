from faker import Faker
from typing import Dict, List, Any
import random
import string
import base64
import uuid
from datetime import datetime, timedelta


class DataGenerator:
    """Generate test data using Faker and custom methods for httpbin.org testing"""
    
    def __init__(self, locale: str = 'en_US'):
        self.faker = Faker(locale)
        Faker.seed(random.randint(0, 10000))
    
    def generate_user(self) -> Dict:
        """Generate random user data"""
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
    
    def generate_post(self) -> Dict:
        """Generate random post data"""
        return {
            "title": self.faker.sentence(nb_words=6),
            "body": self.faker.text(max_nb_chars=200),
            "userId": random.randint(1, 100)
        }
    
    def generate_comment(self) -> Dict:
        """Generate random comment data"""
        return {
            "name": self.faker.sentence(nb_words=4),
            "email": self.faker.email(),
            "body": self.faker.text(max_nb_chars=150)
        }
    
    def generate_random_string(self, length: int = 10) -> str:
        """Generate random string"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def generate_random_number(self, min_val: int = 1, max_val: int = 100) -> int:
        """Generate random number"""
        return random.randint(min_val, max_val)
    
    def generate_email(self) -> str:
        """Generate random email"""
        return self.faker.email()
    
    def generate_phone(self) -> str:
        """Generate random phone number"""
        return self.faker.phone_number()
    
    def generate_users_list(self, count: int = 5) -> List[Dict]:
        """Generate list of users"""
        return [self.generate_user() for _ in range(count)]
    
    def generate_posts_list(self, count: int = 5) -> List[Dict]:
        """Generate list of posts"""
        return [self.generate_post() for _ in range(count)]
    
    def generate_uuid(self) -> str:
        """Generate random UUID"""
        return str(uuid.uuid4())
    
    def generate_base64_string(self, text: str = None) -> str:
        """Generate base64 encoded string"""
        if text is None:
            text = self.faker.text(max_nb_chars=50)
        return base64.b64encode(text.encode()).decode()
    
    def generate_headers(self) -> Dict[str, str]:
        """Generate random HTTP headers"""
        return {
            "User-Agent": self.faker.user_agent(),
            "Accept": random.choice([
                "application/json",
                "application/xml",
                "text/html",
                "text/plain",
                "*/*"
            ]),
            "Accept-Language": random.choice(["en-US", "en-GB", "fr-FR", "de-DE"]),
            "X-Request-ID": self.generate_uuid(),
            "X-Custom-Header": self.generate_random_string(15)
        }
    
    def generate_query_params(self, count: int = 3) -> Dict[str, Any]:
        """Generate random query parameters"""
        params = {}
        for i in range(count):
            key = self.faker.word()
            value_type = random.choice(['string', 'number', 'boolean'])
            
            if value_type == 'string':
                params[key] = self.faker.word()
            elif value_type == 'number':
                params[key] = random.randint(1, 1000)
            else:
                params[key] = random.choice([True, False])
        
        return params
    
    def generate_json_payload(self, complexity: str = 'simple') -> Dict[str, Any]:
        """Generate random JSON payload with varying complexity"""
        if complexity == 'simple':
            return {
                "id": random.randint(1, 1000),
                "name": self.faker.name(),
                "email": self.faker.email(),
                "active": random.choice([True, False])
            }
        elif complexity == 'medium':
            return {
                "id": random.randint(1, 1000),
                "user": {
                    "name": self.faker.name(),
                    "email": self.faker.email(),
                    "username": self.faker.user_name()
                },
                "metadata": {
                    "created_at": self.faker.iso8601(),
                    "updated_at": self.faker.iso8601(),
                    "tags": [self.faker.word() for _ in range(3)]
                },
                "active": random.choice([True, False])
            }
        else:
            return {
                "id": self.generate_uuid(),
                "user": self.generate_user(),
                "posts": [self.generate_post() for _ in range(2)],
                "comments": [self.generate_comment() for _ in range(3)],
                "metadata": {
                    "created_at": self.faker.iso8601(),
                    "updated_at": self.faker.iso8601(),
                    "version": f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}",
                    "tags": [self.faker.word() for _ in range(5)],
                    "settings": {
                        "notifications": random.choice([True, False]),
                        "theme": random.choice(["light", "dark", "auto"]),
                        "language": random.choice(["en", "fr", "de", "es"])
                    }
                }
            }
    
    def generate_form_data(self) -> Dict[str, str]:
        """Generate random form data"""
        return {
            "name": self.faker.name(),
            "email": self.faker.email(),
            "message": self.faker.text(max_nb_chars=200),
            "subject": self.faker.sentence(nb_words=5),
            "phone": self.faker.phone_number()
        }
    
    def generate_delay_value(self, min_delay: int = 1, max_delay: int = 5) -> int:
        """Generate random delay value in seconds"""
        return random.randint(min_delay, max_delay)
    
    def generate_status_code(self, category: str = 'success') -> int:
        """Generate random HTTP status code by category"""
        status_codes = {
            'success': [200, 201, 202, 204],
            'redirect': [301, 302, 303, 307, 308],
            'client_error': [400, 401, 403, 404, 405, 409, 422],
            'server_error': [500, 501, 502, 503, 504]
        }
        return random.choice(status_codes.get(category, [200]))
    
    def generate_auth_credentials(self) -> Dict[str, str]:
        """Generate random authentication credentials"""
        return {
            "username": self.faker.user_name(),
            "password": self.faker.password(length=12, special_chars=True)
        }
    
    def generate_timestamp(self, days_ago: int = 0) -> str:
        """Generate ISO format timestamp"""
        date = datetime.now() - timedelta(days=days_ago)
        return date.isoformat()
    
    def generate_random_bytes(self, size: int = 1024) -> bytes:
        """Generate random bytes data"""
        return random.randbytes(size)
    
    def generate_image_data(self) -> Dict[str, Any]:
        """Generate image metadata"""
        return {
            "format": random.choice(["jpeg", "png", "webp", "svg"]),
            "width": random.choice([100, 200, 300, 400, 500]),
            "height": random.choice([100, 200, 300, 400, 500]),
            "quality": random.randint(50, 100)
        }
