from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import log
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FormsPage(BasePage):
    # Locators
    PRACTICE_FORM_MENU = (By.CSS_SELECTOR, "a[href='/automation-practice-form']")
    
    # Поля формы
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE = (By.ID, "userNumber")
    
    # Date of Birth
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")
    MONTH_SELECT = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_SELECT = (By.CLASS_NAME, "react-datepicker__year-select")
    DAY_CELL = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'day--outside-month'))]")
    
    # Subjects
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    SUBJECTS_SUGGESTION = (By.CLASS_NAME, "subjects-auto-complete__option")
    
    # Hobbies
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    
    # Upload Picture
    UPLOAD_PICTURE = (By.ID, "uploadPicture")
    
    # Current Address
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    
    # State and City
    STATE_DROPDOWN = (By.ID, "state")
    STATE_INPUT = (By.ID, "react-select-3-input")
    CITY_DROPDOWN = (By.ID, "city")
    CITY_INPUT = (By.ID, "react-select-4-input")
    
    # Submit button
    SUBMIT = (By.ID, "submit")
    
    # Modal after submission
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    MODAL_CONTENT = (By.XPATH, "//div[@class='modal-body']//table//td[2]")
    CLOSE_MODAL = (By.ID, "closeLargeModal")

    def open_practice_form(self):
        """Открывает страницу Practice Form через меню Forms."""
        log.info("Opening Practice Form")
        self.click(self.PRACTICE_FORM_MENU)

    def fill_first_name(self, first_name):
        """Вводит имя."""
        log.info(f"Entering first name: {first_name}")
        self.enter_text(self.FIRST_NAME, first_name)

    def fill_last_name(self, last_name):
        """Вводит фамилию."""
        log.info(f"Entering last name: {last_name}")
        self.enter_text(self.LAST_NAME, last_name)

    def fill_email(self, email):
        """Вводит email."""
        log.info(f"Entering email: {email}")
        self.enter_text(self.EMAIL, email)

    def select_gender(self, gender):
        """
        Выбирает пол.        
        """
        log.info(f"Selecting gender: {gender}")
        if gender.lower() == 'male':
            self.click(self.GENDER_MALE)
        elif gender.lower() == 'female':
            self.click(self.GENDER_FEMALE)
        elif gender.lower() == 'other':
            self.click(self.GENDER_OTHER)
        else:
            raise ValueError(f"Invalid gender: {gender}")

    def fill_mobile(self, mobile):
        """Вводит мобильный телефон (только цифры)."""
        log.info(f"Entering mobile: {mobile}")
        self.enter_text(self.MOBILE, mobile)

    def set_date_of_birth(self, month, year, day):
        """
        Устанавливает дату рождения через календарь.      
        """
        log.info(f"Setting date of birth: {month} {day}, {year}")
        self.click(self.DATE_OF_BIRTH_INPUT)
        
        # Выбор месяца
        month_select = self.find_element(self.MONTH_SELECT)
        month_select.click()
        month_option = month_select.find_element(By.XPATH, f"//option[text()='{month}']")
        month_option.click()
        
        # Выбор года
        year_select = self.find_element(self.YEAR_SELECT)
        year_select.click()
        year_option = year_select.find_element(By.XPATH, f"//option[text()='{year}']")
        year_option.click()
        
        # Выбор дня (кликаем по ячейке с нужным числом, исключая дни других месяцев)
        day_element = self.driver.find_element(
            By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'day--outside-month')) and text()='{day}']"
        )
        day_element.click()

    def add_subject(self, subject):
        """
        Добавляет предмет в поле Subjects.        
        """
        log.info(f"Adding subject: {subject}")
        subject_input = self.find_element(self.SUBJECTS_INPUT)
        subject_input.send_keys(subject)
        # Ждем появления подсказки и выбираем первый вариант
        suggestion = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SUBJECTS_SUGGESTION)
        )
        suggestion.click()

    def select_hobby(self, hobby):
        """
        Выбирает хобби (можно вызывать несколько раз).
        """
        log.info(f"Selecting hobby: {hobby}")
        if hobby.lower() == 'sports':
            self.click(self.HOBBIES_SPORTS)
        elif hobby.lower() == 'reading':
            self.click(self.HOBBIES_READING)
        elif hobby.lower() == 'music':
            self.click(self.HOBBIES_MUSIC)
        else:
            raise ValueError(f"Invalid hobby: {hobby}")

    def upload_picture(self, file_path):
        """
        Загружает картинку.        
        """
        log.info(f"Uploading picture: {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        upload_element = self.find_element(self.UPLOAD_PICTURE)
        upload_element.send_keys(file_path)

    def fill_current_address(self, address):
        """Вводит текущий адрес."""
        log.info(f"Entering current address: {address}")
        self.enter_text(self.CURRENT_ADDRESS, address)

    def select_state(self, state):
        """
        Выбирает штат из выпадающего списка.       
        """
        log.info(f"Selecting state: {state}")
        self.click(self.STATE_DROPDOWN)
        state_input = self.find_element(self.STATE_INPUT)
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, city):
        """
        Выбирает город из выпадающего списка.       
        """
        log.info(f"Selecting city: {city}")
        self.click(self.CITY_DROPDOWN)
        city_input = self.find_element(self.CITY_INPUT)
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def submit_form(self):
        """Отправляет форму."""
        log.info("Submitting the form")
        # Чтобы избежать перекрытия баннером, можно проскроллить до кнопки
        submit_btn = self.find_element(self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        submit_btn.click()

    def get_modal_title(self):
        """Возвращает заголовок модального окна после отправки."""
        return self.get_text(self.MODAL_TITLE)

    def get_modal_data(self):
        """
        Возвращает данные из модального окна в виде словаря.        
        """
        log.info("Fetching modal data")
        rows = self.driver.find_elements(By.XPATH, "//div[@class='modal-body']//tr")
        data = {}
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                label = cells[0].text.strip().replace(':', '')
                value = cells[1].text.strip()
                data[label] = value
        return data
      

    def close_modal(self):
        """Закрывает модальное окно."""
        log.info("Closing modal")
        self.click(self.CLOSE_MODAL)

    def fill_full_form(self, student_data):
        """
        Заполняет всю форму целиком, используя переданный словарь с данными.        
        """
        self.fill_first_name(student_data['first_name'])
        self.fill_last_name(student_data['last_name'])
        self.fill_email(student_data['email'])
        self.select_gender(student_data['gender'])
        self.fill_mobile(student_data['mobile'])
        self.set_date_of_birth(student_data['month'], student_data['year'], student_data['day'])
        
        for subject in student_data.get('subjects', []):
            self.add_subject(subject)
        
        for hobby in student_data.get('hobbies', []):
            self.select_hobby(hobby)
        
        if 'picture_path' in student_data:
            self.upload_picture(student_data['picture_path'])
        
        self.fill_current_address(student_data['current_address'])
        self.select_state(student_data['state'])
        self.select_city(student_data['city'])
        
        self.submit_form()