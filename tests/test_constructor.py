from locators import Locators


class Test_constructor:

    active_class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_burger_section(self, driver, autorization, constructor):
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        driver.find_element(*Locators.BURGERS_BUTTON).click()
        assert driver.find_element(*Locators.BURGERS_BUTTON).get_attribute('class') == self.active_class

    def test_sauces_section(self, driver, autorization, constructor):
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        assert driver.find_element(*Locators.SAUCE_BUTTON).get_attribute('class') == self.active_class

    def test_toppings_section(self, driver, autorization, constructor):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        assert driver.find_element(*Locators.TOPPINGS_BUTTON).get_attribute('class') == self.active_class
