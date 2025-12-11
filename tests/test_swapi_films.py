import pytest
import allure
from src.api.swapi_client import SwapiClient
from utils.pytest_retry import retry_flaky_test


@allure.feature('SWAPI - Star Wars API')
class TestSwapiFilms:    
    @allure.title("Test get all films")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_films(self, swapi_client):
        with allure.step("Send GET request to /films endpoint"):
            response = swapi_client.get_all_films()
        
        with allure.step("Verify response status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        with allure.step("Verify response is valid JSON"):
            json_data = response.json()
            assert isinstance(json_data, dict), "Response should be a JSON object"
        
        with allure.step("Verify response structure"):
            assert 'count' in json_data, "Response should contain 'count' field"
            assert 'results' in json_data, "Response should contain 'results' field"
            assert isinstance(json_data['results'], list), "'results' should be a list"
        
        with allure.step("Verify films count"):
            assert json_data['count'] == 6, f"Expected 6 films, got {json_data['count']}"
            assert len(json_data['results']) == 6, f"Expected 6 films in results, got {len(json_data['results'])}"
        
        allure.attach(
            response.text,
            name="Films Response",
            attachment_type=allure.attachment_type.JSON
        )
    
    @allure.title("Test specific film - A New Hope")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_specific_film(self, swapi_client):
        with allure.step("Send GET request to /films/1/ endpoint"):
            response = swapi_client.get_film_by_id(1)
        
        with allure.step("Verify response status code is 200"):
            assert response.status_code == 200
        
        with allure.step("Verify film details"):
            film = response.json()
            assert film['title'] == "A New Hope", f"Expected 'A New Hope', got {film['title']}"
            assert film['episode_id'] == 4, f"Expected episode 4, got {film['episode_id']}"
            assert film['director'] == "George Lucas"
        
        allure.attach(
            response.text,
            name="A New Hope Details",
            attachment_type=allure.attachment_type.JSON
        )

    # this test is expected to fail (flaky test to show retry logic)
    @allure.title("Test invalid film ID")
    @allure.severity(allure.severity_level.NORMAL)
    @retry_flaky_test()
    def test_invalid_film_id(self, swapi_client):
        with allure.step("Send GET request with invalid film ID"):
            response = swapi_client.get_film_by_id(999)
        
        with allure.step("Verify response status code is 200"):
            assert response.status_code == 200, f"Expected 200 for invalid ID, got {response.status_code}"
