# Test Automation Framework

Test automation framework built with pytest, featuring custom retry logic and Allure reporting.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+ (tested on 3.9, 3.10, 3.11)
- pip (Python package manager)
- Git

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
Copy and edit `.env` file:
```bash
cp .env.example .env
```

Edit `.env` file with your settings


## 🧪 Running Tests

```bash
# Run all tests
pytest -v

# Run with Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

## 📁 Project Structure

```
python-simple-test-framework/
├── conftest.py                    # Pytest fixtures
├── pytest.ini                     # Pytest settings
├── requirements.txt               # Dependencies
├── .env                           # Environment variables
├── src/
│   └── api/
│       ├── base_client.py        # Base HTTP client (CRUD)
│       └── swapi_client.py       # SWAPI client
├── tests/
│   └── test_swapi_films.py       # Films endpoint tests
└── utils/
    ├── config_loader.py          # Config from .env
    └── pytest_retry.py           # Retry decorator

## 🔧 Usage Example

```python
from src.api.swapi_client import SwapiClient
from utils.pytest_retry import retry_flaky_test

@retry_flaky_test()
def test_get_all_films(swapi_client):
    response = swapi_client.get_all_films()
    assert response.status_code == 200
    assert response.json()['count'] == 6
```
