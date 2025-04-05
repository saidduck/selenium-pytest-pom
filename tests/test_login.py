from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.config import Config
import time

class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        request.cls.driver = webdriver.Chrome()  # You can change this to your preferred WebDriver
        request.cls.driver.get(Config.URL)
        request.cls.login_page = LoginPage(request.cls.driver)
        time.sleep(5)  # Wait for the page to load    
        yield
        request.cls.driver.quit()

    def test_login_success(self):
        self.login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        time.sleep(5)
        assert self.login_page.is_login_successful() == True

    def test_login_failure(self):
        self.login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        time.sleep(5)
        assert self.login_page.is_login_successful() == False