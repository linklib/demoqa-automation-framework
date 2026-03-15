from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ElementsPage(BasePage):
    # Locators
    TEXT_BOX_MENU = (By.XPATH, "//span[text()='Text Box']")
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")

    def open_text_box(self):
        self.click(self.TEXT_BOX_MENU)

    def fill_text_box(self, name, email, current_addr, perm_addr):
        self.enter_text(self.FULL_NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.CURRENT_ADDRESS, current_addr)
        self.enter_text(self.PERMANENT_ADDRESS, perm_addr)
        self.click(self.SUBMIT)

    def get_output_data(self):
        return {
            "name": self.get_text(self.OUTPUT_NAME).replace("Name:", "").strip(),
            "email": self.get_text(self.OUTPUT_EMAIL).replace("Email:", "").strip(),
            "current_address": self.get_text(self.OUTPUT_CURRENT_ADDRESS).replace("Current Address :", "").strip(),
            "permanent_address": self.get_text(self.OUTPUT_PERMANENT_ADDRESS).replace("Permananet Address :", "").strip()
        }