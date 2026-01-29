import pytest
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import browser
from dotenv import load_dotenv
from utils import attach


@pytest.fixture(scope="function", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def browser_set():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.config.base_url = 'https://demo.nopcommerce.com'
    browser.config.window_width = 2560
    browser.config.window_height = 1440


    yield

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)
    attach.add_video(driver)

    browser.quit()