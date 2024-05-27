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

# @pytest.fixture(random_login, random_password)
# def registration(random_login, random_password):
#     driver = webdriver.Chrome()
#     driver.get("https://stellarburgers.nomoreparties.site/register")
#     # Заполнить все поля
#     driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input").send_keys("name")
#     driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys(random_login)
#     driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(random_password)
#     # Нажать "Зарегистрированиться"
#     driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
#     driver.quit()
#     registration = {"name": "name",
#                     "login": random_login,
#                     "password": random_password}
#     return registration
