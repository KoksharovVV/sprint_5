import pytest
import data
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRegistrarionPage:

    def test_registration(self, random_user, driver):
        driver.get(data.url["registration_page"])
        # Заполнить все поля
        driver.find_element(*TestLocators.INPUT_NAME).send_keys("name")
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_user["login"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_user["password"])
        # Нажать "Зарегистрированиться"
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(TestLocators.BUTTON_FORGOT_PASSWORD))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_user["login"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_user["password"])
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_SIGN_IN))
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        url = driver.current_url
        assert url == data.url["main_page"]

    @pytest.mark.parametrize("login, password, res", [
        ("pupupu_tututu9mail.ru", "123456", "Неправильный формат электронной почты"),
        ("pupupu_tututu9123@mail.ru", "12345", "Некорректный пароль")
    ])
    def test_registration_invalid_data(self, login, password, res, driver):
        driver.get(data.url["registration_page"])
        # Заполнить все поля
        driver.find_element(*TestLocators.INPUT_NAME).send_keys("name")
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        # Нажать "Зарегистрированиться"
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(TestLocators.ERROR_REGISTRATION))
        txt = driver.find_element(*TestLocators.ERROR_REGISTRATION).text
        # Проверить текст ошибки после регистрации
        assert txt == res
