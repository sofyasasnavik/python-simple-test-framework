import pytest
import logging
import allure
from datetime import datetime
from pathlib import Path
from utils.config_loader import config as app_config
from src.api.swapi_client import SwapiClient


def pytest_configure(config):
    """Configure pytest with custom settings"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    allure_dir = Path("allure-results")
    allure_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"test_run_{timestamp}.log"
    
    logging.basicConfig(
        level=getattr(logging, app_config.log_level),
        format='%(asctime)s | %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("="*100)
    logger.info(f"TEST RUN STARTED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*100)


@pytest.fixture(scope="session")
def logger():
    """Provide logger fixture for tests"""
    return logging.getLogger(__name__)


@pytest.fixture(scope="session")
def swapi_client():
    """Provide SwapiClient instance for tests"""
    client = SwapiClient()
    yield client
    client.close()


@pytest.fixture(scope="function", autouse=True)
def test_setup_teardown(request, logger):
    """Setup and teardown for each test"""
    test_name = request.node.name    
    logger.info(f"TEST STARTED: {test_name}")
    
    start_time = datetime.now()
    yield
    duration = (datetime.now() - start_time).total_seconds()
    
    logger.info(f"TEST FINISHED: {test_name} | Duration: {duration:.2f}s")
    logger.info("-" * 100)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to attach failure details to Allure reports"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        if hasattr(report, 'longreprtext'):
            allure.attach(
                report.longreprtext,
                name="Failure Details",
                attachment_type=allure.attachment_type.TEXT
            )


def pytest_sessionfinish(session, exitstatus):
    """Log test run summary at the end"""
    logger = logging.getLogger(__name__)
    
    total = session.testscollected if hasattr(session, 'testscollected') else 0
    failed = session.testsfailed if hasattr(session, 'testsfailed') else 0
    skipped = session.testsskipped if hasattr(session, 'testsskipped') else 0
    passed = total - failed - skipped
    
    logger.info("="*100)
    logger.info(f"TEST RUN FINISHED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Total: {total} | Passed: {passed} | Failed: {failed} | Skipped: {skipped}")
    logger.info("="*100)
