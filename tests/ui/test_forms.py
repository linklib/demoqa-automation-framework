import allure
import os
from pages.forms_page import FormsPage
import time

@allure.feature("Forms")
@allure.story("Practice Form")
def test_practice_form(driver):
    page = FormsPage(driver)
    page.open("https://demoqa.com/forms")
    page.open_practice_form()

    #Определяем абсолютный путь к аватарке
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    image_path = os.path.join(project_root, "ava.jpg")

    student = {
        "first_name": "Иван",
        "last_name": "Петров",
        "email": "ip_petrov@example.com",
        "gender": "Male",
        "mobile": "1234567890",
        "month": "May",
        "year": "1990",
        "day": "15",
        "subjects": ["Maths", "English"],
        "hobbies": ["Sports", "Reading"],
        "picture_path": image_path,
        "current_address": "109001 Kremlin",
        "state": "NCR",
        "city": "Delhi"
    }


    page.fill_full_form(student)
#TODO: убрать спипы, добавить ожидание в фукцию открытия модалки    
    time.sleep(2)
    assert page.get_modal_title() == "Thanks for submitting the form"
    modal_data = page.get_modal_data()
    assert modal_data["Student Name"] == "Иван Петров"
    assert modal_data["Student Email"] == "ip_petrov@example.com"
    assert modal_data["Gender"] == "Male"
    assert modal_data["Mobile"] == "1234567890"
    assert modal_data["Date of Birth"] == "15 May,1990"
    assert modal_data["Subjects"] == "Maths, English"
    assert modal_data["Hobbies"] == "Sports, Reading"
    assert modal_data["Picture"] == "ava.jpg"
    assert modal_data["Address"] == "109001 Kremlin"
    assert modal_data["State and City"] == "NCR Delhi"
#TODO: проверить кнопку закрытия
    page.close_modal()
    time.sleep(2)
