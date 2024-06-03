import pytest
from locators import TestLocators
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuthorizationPage:
    @pytest.mark.parametrize("cond",[
        TestLocators.BUTTON_PERSONAL_AREA,
        TestLocators.BUTTON_LOGIN_ACCOUNT
    ])
    def test_auth_via_main_page(self, driver, cond):
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к авторизации
        driver.find_element(*cond).click()
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
        text = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER).text
        assert text == "Оформить заказ"

    def test_auth_via_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        # Нажать "Войти"
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
        text = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER).text
        assert text == "Оформить заказ"

    def test_auth_via_form_restore_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        # Перейти к форме восстановления пароля
        driver.find_element(*TestLocators.BUTTON_FORGOT_PASSWORD).click()
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
        text = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER).text
        assert text == "Оформить заказ"
