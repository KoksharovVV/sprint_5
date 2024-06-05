import pytest
from locators import TestLocators
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestPersonalAreaPage:
    @pytest.mark.parametrize("locator", [
        TestLocators.BUTTON_CONSTRUCTION,
        TestLocators.LOGO
    ])
    def test_transition_constructor_from_personal_area(self, locator, driver):
        driver.get(data.url["main_page"])
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_AREA))
        # Перейти к авторизации
        driver.find_element(*TestLocators.BUTTON_PERSONAL_AREA).click()
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_AREA))
        # Перейти в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        url = driver.current_url
        assert url == data.url["main_page"]

    def test_exit(self, driver):
        driver.get(data.url["login_page"])
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_AREA))
        # Перейти в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_AREA).click()
        # Жмем кнопку "Выход"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_EXIT))
        driver.find_element(*TestLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(TestLocators.BUTTON_SIGN_IN))
        url = driver.current_url
        assert url == data.url["login_page"]
