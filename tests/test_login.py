from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.config import Config

class TestLogin:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()  # You can change this to your preferred WebDriver
        self.driver.get(Config.URL)
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_login_success(self, setup):
        self.login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        assert self.login_page.is_login_successful() == True

    def test_login_failure(self, setup):
        self.login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        assert self.login_page.is_login_successful() == False