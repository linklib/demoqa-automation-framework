import allure
from api.account_api import AccountAPI

@allure.feature("API Account")
def test_create_user(api_client, new_user_data):
    account_api = AccountAPI(api_client)
    response = account_api.create_user(new_user_data)
    assert response.status_code == 201
    assert response.json()["username"] == new_user_data["userName"]

@allure.feature("API Account")
def test_generate_token(api_client, new_user_data):
    # Сначала создаем пользователя
    account_api = AccountAPI(api_client)
    account_api.create_user(new_user_data)
    # Генерируем токен
    response = account_api.generate_token(new_user_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert "token" in response.json()