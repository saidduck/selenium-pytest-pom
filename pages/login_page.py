class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.dashboard_header = "h6"  # Example locator for dashboard header after login
        self.error_message = ".oxd-alert"  # Example locator for error message

    def enter_username(self, username):
        self.driver.find_element("css selector", self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("css selector", self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element("css selector", self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        return self.driver.find_element("css selector", self.dashboard_header).is_displayed()

    def is_login_failed(self):
        return self.driver.find_element("css selector", self.error_message).is_displayed()