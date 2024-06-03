import pytest
import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(executable_path="/Users/vovak/chromedriver/chromedriver-win64/chromedriver.exe")
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def data():
    user = {}
    user["login"] = f'namesername{random.randint(0, 9)}{random.randint(0, 999)}@yandex.ru'
    user["password"] = str(random.randint(100000, 999999))
    with open('random_login_details.json', 'w') as file:
        json.dump(user, file)
    with open('random_login_details.json', 'r') as file:
        user = json.load(file)
        data = {"login": user["login"],
                "password": user["password"]}
    return data

