import pytest
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
def random_user():
    random_user = {}
    random_user["login"] = f'namesername{random.randint(0, 9)}{random.randint(0, 999)}@yandex.ru'
    random_user["password"] = str(random.randint(100000, 999999))
    return random_user
