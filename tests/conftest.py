import pytest
from core.web_driver import init_driver
from core.api_client import APIClient
from config.settings import BASE_URL, API_URL
from config.test_data import generate_user
from utils.logger import log

@pytest.fixture(scope="function")
def driver():
    driver = init_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_client():
    return APIClient(API_URL)

@pytest.fixture
def new_user_data():
    return generate_user()

@pytest.fixture
def auth_token(api_client, new_user_data):
    """Создает пользователя и возвращает токен"""
    # Создаем пользователя
    resp = api_client.post("/Account/v1/User", json=new_user_data)
    assert resp.status_code == 201
    user_id = resp.json()["userID"]
    # Генерируем токен
    resp = api_client.post("/Account/v1/GenerateToken", json=new_user_data)
    assert resp.status_code == 200
    token = resp.json()["token"]
    return {"user_id": user_id, "token": token, "user_data": new_user_data}