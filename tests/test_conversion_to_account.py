from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Test_personal_account:

    def test_profile_button(self, driver, autorization):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_HISTORY))
        assert "История заказов" in title.text

