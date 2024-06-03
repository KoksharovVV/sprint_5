import pytest
from selenium.common import ElementClickInterceptedException
from locators import TestLocators
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:
    def test_transition_personal_area(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к авторизации
        driver.find_element(*TestLocators.BUTTON_PERSONAL_AREA).click()
        # Заполнить поля для авторизации
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(data.user_data['email'])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(data.user_data['password'])
        driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_AREA))
        # Перейти в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.BUTTON_SAVE))
        text = driver.current_url
        assert text == "https://stellarburgers.nomoreparties.site/account/profile"

    @pytest.mark.parametrize("locator", (
            TestLocators.BUTTON_SAUCE,
            TestLocators.BUTTON_FILLING,
            TestLocators.BUTTON_BUN
    ))
    def test_constructor_transition(self, locator, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Нажать на раздел в конструкторе
        # Блок try используется, потому что выбранный таб является некликабельным
        try:
            driver.find_element(*locator).click()
        except ElementClickInterceptedException:
            cls = driver.find_element(*locator).get_attribute("class")
        finally:
            cls = driver.find_element(*locator).get_attribute("class")
        assert cls == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
