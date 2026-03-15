from core.api_client import APIClient

class AccountAPI:
    def __init__(self, api_client):
        self.client = api_client

    def create_user(self, user_data):
        return self.client.post("/Account/v1/User", json=user_data)

    def generate_token(self, user_data):
        return self.client.post("/Account/v1/GenerateToken", json=user_data)

    def get_user(self, user_id, token):
        self.client.set_token(token)
        return self.client.get(f"/Account/v1/User/{user_id}")
