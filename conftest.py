import pytest
from selene import browser
from selenium import webdriver
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.driver_options = webdriver.ChromeOptions()
    #browser.config.driver_options.page_load_strategy = 'eager'
    #browser.config.driver_options.add_argument("--headless")
    #browser.config.base_url = "https://demoqa.com"
    browser.driver.maximize_window()

    yield

    browser.quit()