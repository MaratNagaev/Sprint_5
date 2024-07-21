from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class Test_registration:

    def test_registration(self, driver, registration):
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_3))
        assert 'Войти' in title.text

    def test_registration_false(self, driver, registration):
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))
        assert 'Некорректный пароль' in title.text

