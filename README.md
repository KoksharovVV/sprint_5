# sprint_5
# # Проект автоматизации тестирования Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest.
2. Вспомогательный фреймворк для автоматизации работы с браузером - selenium
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 

# #Тесты-кейсы в проекте
1. Регистрация
   1. Регистрация с валидными данными
   2. Регистрация с невалидным паролем
   3. Регистрация с невалидной почтой 
2. Авторизация
   1. Вход по кнопке "Войти в аккаунт" на главной странице
   2. Вход через кнопку "Личный кабинет"
   3. Вход через кнопку в форме регестрации
   4. Вход через кнопку в форме восстановление пароля
3. Переход в личный кабинет по клику на "Личный кабинет"
4. Переход в "Конструктор"
   1. Переход по клику на "Конструктор"
   2. Переход по клику на логотип Stellar Burgers
5. Выход из аккаунта
6. Раздел "Конструктор", проверить переходы
   1. Проверить переход к разделу "Булки"
   2. Проверить переход к разделу "Соусы"
   3. Проверить переход к разделу "Начинки"