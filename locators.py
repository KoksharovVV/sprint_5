from selenium.webdriver.common.by import By


class TestLocators:
    INPUT_NAME = (By.XPATH, ".//label[text()='Имя']/parent::div/input")  # Поиск поля "Имя"
    INPUT_EMAIL = (By.XPATH, ".//label[text()='Email']/parent::div/input")  # Поиск поля "e-mail"
    BUTTON_PERSONAL_AREA = (By.XPATH, ".//*[text()='Личный Кабинет']")  # Поиск кнопки "Личный кабинет"
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")  # Поиск поля "Пароль"
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Поиск кнопки "Зарегистрироваться"
    BUTTON_SIGN_IN = (By.XPATH, ".//*[text()='Войти']")  # Поиск кнопки "Войти"
    BUTTON_EXIT = (By.XPATH, ".//*[text()='Выход']")  # Поиск кнопки "Выйти"
    ERROR_REGISTRATION = (By.CSS_SELECTOR, ".input__error")  # Поиск элемента с ошибкой
    BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")  # Поиск перехода к "Восстановление пароля"
    BUTTON_SAVE = (By.XPATH, ".//button[text()='Сохранить']")  # Поиск кнопки "Сохранить"
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, ".//*[text()='Войти в аккаунт']")  # Поиск кнопки "Войти в аккаунт"
    BUTTON_MAKE_AN_ORDER = (By.XPATH, ".//*[text()='Оформить заказ']")  # Поиск кнопки "Оформить заказ"
    BUTTON_SAUCE = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Поиск раздела "Соусы"
    BUTTON_FILLING = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Поиск раздела "Начинки"
    BUTTON_BUN = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Поиск раздела "Булки"
    BUTTON_CONSTRUCTION = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")   # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип
