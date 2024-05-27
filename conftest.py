import pytest
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture()
def random_login():
    random_login = f'namesername{random.randint(0,9)}{random.randint(0,999)}@yandex.ru'
    return random_login
@pytest.fixture()
def random_password():
    random_password = str(random.randint(100000, 999999))
    return random_password
