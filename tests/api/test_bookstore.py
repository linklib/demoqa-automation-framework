import allure
from api.account_api import AccountAPI
from api.bookstore_api import BookstoreAPI

@allure.feature("API Bookstore")
def test_add_books_to_user(api_client, auth_token):
    account_api = AccountAPI(api_client)
    bookstore_api = BookstoreAPI(api_client)

    user_id = auth_token["user_id"]
    token = auth_token["token"]

    # Получаем список книг
    books_resp = bookstore_api.get_books()
    assert books_resp.status_code == 200
    books = books_resp.json()["books"]
    assert len(books) > 0

    # Добавляем первую книгу
    isbn = books[0]["isbn"]
    add_resp = bookstore_api.add_books(user_id, [isbn], token)
    assert add_resp.status_code == 201

    # Проверяем, что книга добавилась (получаем профиль пользователя)
    user_resp = account_api.get_user(user_id, token)
    assert user_resp.status_code == 200
    user_books = user_resp.json()["books"]
    assert any(book["isbn"] == isbn for book in user_books)

    # Очищаем коллекцию
    del_resp = bookstore_api.delete_books(user_id, token)
    assert del_resp.status_code == 204