# DemoQA Automation Framework (UI + API)

Проект представляет собой фреймворк для автоматизированного тестирования сайта [DemoQA](https://demoqa.com/).  
Реализованы тесты UI (Selenium) и API (Requests) с использованием паттерна Page Object, фикстур Pytest, логирования и генерации отчётов Allure.

## Технологии
- Python 3.10+
- Pytest
- Selenium WebDriver
- Requests
- Allure
- GitHub Actions (CI)

## Установка и запуск

1. Клонировать репозиторий:
git clone https://github.com/linklib/demoqa-automation-framework.git
cd demoqa-automation-framework

2. Создать виртуальное окружение и установить зависимости:
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt

3. Создать файл .env на основе .env.example и при необходимости изменить настройки.

4. Запустить тесты:
pytest

5. Сформировать Allure отчёт:
allure serve allure-results