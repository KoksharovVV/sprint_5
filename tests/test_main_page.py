import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestMainPage:
    def test_transition_personal_area(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к авторизации
        driver.find_element(By.XPATH,
                            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                            "button_button_size_large__G21Vg']").click()
        # Заполнить поля для авторизации
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys("koksharov_9555@mail.ru")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123123")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[@href='/account']")))
        # Перейти в личный кабинет
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Сохранить']")))
        text = driver.current_url
        driver.quit()
        assert text == "https://stellarburgers.nomoreparties.site/account/profile"

    @pytest.mark.parametrize("locator", (
            ".//span[text()='Соусы']/parent::div",
            ".//span[text()='Начинки']/parent::div",
    ))
    def test_constructor_transition(self, locator):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Нажать на раздел в конструкторе
        driver.find_element(By.XPATH, locator).click()
        cls = driver.find_element(By.XPATH, locator).get_attribute("class")
        driver.quit()
        assert cls == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_constructor_transition_to_bread(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к кликабельному разделу
        driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").click()
        # Перейти к разделу "Булки"
        driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").click()
        cls = driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").get_attribute("class")
        driver.quit()
        assert cls == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'