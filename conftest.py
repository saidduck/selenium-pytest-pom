from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def browser():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()  # You can change this to any other WebDriver as needed
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    # Teardown: Quit the WebDriver
    driver.quit()