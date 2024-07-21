import pytest
from selenium import webdriver
from locators import Locators
import random
from config import email, password, url


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()

@pytest.fixture()
def registration(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_1).click()
    driver.find_element(*Locators.LOGIN_BUTTON_2).click()

    # Заполняем поля формы регистрации
    driver.find_element(*Locators.NAME_INPUT).send_keys("Marat Nagaev")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(f"marat_nagaev_11_{random.randint(100, 999)}@yandex.ru")

    return driver

@pytest.fixture()
def autorization(driver):
    driver.get(f'{url}login')
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON_3).click()

@pytest.fixture()
def constructor(driver):
    driver.find_element(*Locators.BUILDER_BUTTON).click()


