from core.api_client import APIClient

class BookstoreAPI:
    def __init__(self, api_client):
        self.client = api_client

    def get_books(self):
        return self.client.get("/BookStore/v1/Books")

    def add_books(self, user_id, books_isbns, token):
        self.client.set_token(token)
        data = {
            "userId": user_id,
            "collectionOfIsbns": [{"isbn": isbn} for isbn in books_isbns]
        }
        return self.client.post("/BookStore/v1/Books", json=data)

    def delete_books(self, user_id, token):
        self.client.set_token(token)
        return self.client.delete(f"/BookStore/v1/Books?UserId={user_id}") 