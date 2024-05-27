import pytest
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

def test_registration():
    # Открыть форму регистрации
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    # Заполнить все поля
    driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input").send_keys("name")
    driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys("email@mail.ru")
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123123")
    # Нажать "Зарегистрированиться"
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    sleep(4)
    driver.quit()
