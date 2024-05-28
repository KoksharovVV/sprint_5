import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorizationPage:
    @pytest.mark.parametrize("location_auth", [
        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']",
        ".//a[@href='/account']"
    ])
    def test_auth_via_main_page(self, location_auth):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к авторизации
        driver.find_element(By.XPATH, location_auth).click()
        # Заполнить поля для авторизации
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys("koksharov_9555@mail.ru")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123123")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                                             ".//button[@class='button_button__33qZ0 "
                                                             "button_button_type_primary__1O7Bx "
                                                             "button_button_size_large__G21Vg']")))
        text = driver.find_element(By.XPATH,
                                   ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                   "button_button_size_large__G21Vg']").text
        driver.quit()
        assert text == "Оформить заказ"

    def test_auth_via_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        # Нажать "Войти"
        driver.find_element(By.XPATH, ".//a[@href='/login']").click()
        # Заполнить поля для авторизации
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys("koksharov_9555@mail.ru")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123123")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                                             ".//button[@class='button_button__33qZ0 "
                                                             "button_button_type_primary__1O7Bx "
                                                             "button_button_size_large__G21Vg']")))
        text = driver.find_element(By.XPATH,
                                   ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                   "button_button_size_large__G21Vg']").text
        driver.quit()
        assert text == "Оформить заказ"

    def test_auth_via_form_restore_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти к авторизации
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        # Перейти к форме восстановления пароля
        driver.find_element(By.XPATH, ".//a[@href='/forgot-password']").click()
        driver.find_element(By.XPATH, ".//a[@href='/login']").click()
        # Заполнить поля для авторизации
        driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys("koksharov_9555@mail.ru")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123123")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                                             ".//button[@class='button_button__33qZ0 "
                                                             "button_button_type_primary__1O7Bx "
                                                             "button_button_size_large__G21Vg']")))
        text = driver.find_element(By.XPATH,
                                   ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                   "button_button_size_large__G21Vg']").text
        driver.quit()
        assert text == "Оформить заказ"
