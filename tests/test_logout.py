from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url
from locators import Locators


class Test_exit:

    def test_logout(self, driver, autorization):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_LOGIN))
        assert driver.current_url == f'{url}login'




