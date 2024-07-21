from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url
from locators import Locators


class Test_login:

    def test_login_through_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_1).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))
        assert driver.current_url == f'{url}login'

    def test_login_through_profile_button(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))
        assert driver.current_url == f'{url}login'

    def test_login_through_registration_form(self, driver):
        driver.get(f'{url}register')
        driver.find_element(*Locators.REG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))
        assert driver.current_url == f'{url}login'

    def test_login_through_recovery_to_password(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_1).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))

        driver.find_element(*Locators.BUTTON_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_RECOVERY_PASSWORD))

        driver.find_element(*Locators.REC_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))
        assert driver.current_url == f'{url}login'

    def test_successful_login(self, driver, autorization):
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert 'Оформить заказ' in title.text



