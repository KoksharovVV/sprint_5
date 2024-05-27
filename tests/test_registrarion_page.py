import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistrarionPage:

    def test_registration(self, random_login, random_password):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполнить все поля
        driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input").send_keys("name")
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys(random_login)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(random_password)
        # Нажать "Зарегистрированиться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        current_url = driver.current_url
        # Проверить url после регистрации
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        # Проверить авторизацию зарегистрированного аккаунта
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys(random_login)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(random_password)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    @pytest.mark.parametrize("login, password, res", [
        ("pupupu_tututu9mail.ru", "123456", "Неправильный формат электронной почты"),
        ("pupupu_tututu9123@mail.ru", "12345", "Некорректный пароль")
    ])
    def test_registration_invalid_data(self, login, password, res):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполнить все поля
        driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input").send_keys("name")
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
        # Нажать "Зарегистрированиться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".input__error")))
        txt = driver.find_element(By.CSS_SELECTOR, ".input__error").text
        driver.quit()
        # Проверить текст ошибки после регистрации
        assert txt == res
