from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url
from locators import Locators


class Test_logo_and_constructor:

    def test_constructor_button(self, driver, autorization, constructor):
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUILDER_TITLE))
        assert "Соберите бургер" in title.text

    def test_logo_button(self, driver, autorization):
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUILDER_TITLE))
        assert driver.current_url == url

