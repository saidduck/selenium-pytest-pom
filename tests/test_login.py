from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from utils.config import Config

class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        request.cls.driver = webdriver.Chrome()  # You can change this to your preferred WebDriver
        request.cls.driver.get(Config.URL)
        request.cls.login_page = LoginPage(request.cls.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input-group__label-wrapper"))  # Replace with the actual locator
        )
        yield
        request.cls.driver.quit()

    def test_login_failure(self):
        self.login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        # Wait for the login failure message or condition
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content.oxd-alert-content--error"))  # Replace with the actual locator
        )
        assert self.login_page.is_login_failed() == True

    def test_login_success(self):
        self.login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        # Wait for the login success condition
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"))  # Replace with the actual locator
        )
        assert self.login_page.is_login_successful() == True
