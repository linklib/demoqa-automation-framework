import allure
from pages.elements_page import ElementsPage

@allure.feature("Elements")
@allure.story("Text Box")
def test_text_box(driver):
    page = ElementsPage(driver)
    page.open("https://demoqa.com/elements")
    page.open_text_box()

    test_data = {
        "name": "Иван Петров",
        "email": "ip_petrov@example.com",
        "current_addr": "109001 Kremlin",
        "perm_addr": "123123 Begichevo"
    }

    page.fill_text_box(**test_data)

    output = page.get_output_data()
    assert output["name"] == test_data["name"]
    assert output["email"] == test_data["email"]
    assert output["current_address"] == test_data["current_addr"]
    assert output["permanent_address"] == test_data["perm_addr"]