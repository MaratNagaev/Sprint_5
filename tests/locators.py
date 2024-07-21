from selenium.webdriver.common.by import By


class Locators:
    # Страница входа
    PAGE_LOGIN = (By.XPATH, './/h2[text()="Вход"]')

    # Страница восстановления пароля
    PAGE_RECOVERY_PASSWORD = (By.XPATH, './/main[@class="App_componentContainer__2JC2W"]')

    # Кнопка оформить заказ
    BUTTON_ORDER = (By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

    # Кнопка войти в тайтле регистрации
    REG_LOGIN_BUTTON = (By.XPATH, './/a[@class = "Auth_link__1fOlj"]')

    # Кнопка «Войти»
    LOGIN_BUTTON_1 = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    LOGIN_BUTTON_2 = (By.XPATH, './/a[@class="Auth_link__1fOlj" and  text()="Зарегистрироваться"]')

    # Кнопка восстановления пароля
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, './/a[@class="Auth_link__1fOlj" and  text()="Восстановить пароль"]')

    # Кнопка войти в странице восстановления пароля
    REC_LOGIN_BUTTON = (By.XPATH, './/a[@class = "Auth_link__1fOlj"]')

    # Поле ввода имени
    NAME_INPUT = (By.XPATH, './/fieldset[1]/div/div/input')

    # Поле ввода электронной почты
    EMAIL_INPUT = (By.XPATH, './/fieldset[2]/div/div/input')

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, './/fieldset[3]/div/div/input')

    # Поле ввода email для входа
    LOGIN_EMAIL_INPUT = (By.NAME, 'name')

    # Поле ввода password для входа
    LOGIN_PASSWORD_INPUT = (By.NAME, 'Пароль')

    # Кнопка «Регистрация»
    REGISTER_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Зарегистрироваться"]')
    LOGIN_BUTTON_3 = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]')
    ERROR_MESSAGE = (By.XPATH, './/p[@class="input__error text_type_main-default"]')

    # Кнопка «Личный кабинет»
    PROFILE_BUTTON = (By.XPATH, './/a[@href="/account"]/p[@class ="AppHeader_header__linkText__3q_va ml-2"]')

    # Кнопка Истории заказов
    BUTTON_HISTORY = (By.XPATH, './/a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive"]')

    # Кнопка «Конструктор»
    BUILDER_BUTTON = (By.XPATH, './/a[@href="/"]/p[@class ="AppHeader_header__linkText__3q_va ml-2"]')
    BUILDER_TITLE = (By.XPATH, './/h1')

    # Кнопка логотипа
    LOGO_BUTTON = (By.XPATH, './/div[@class = "AppHeader_header__logo__2D0X2"]')

    # Кнопка «Выйти»
    LOGOUT_BUTTON = (By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')

    # Переход к разделам: «Булки», «Соусы», «Начинки»
    BURGERS_BUTTON = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Булки"]/..')
    SAUCE_BUTTON = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Соусы"]/..')
    TOPPINGS_BUTTON = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Начинки"]/..')

