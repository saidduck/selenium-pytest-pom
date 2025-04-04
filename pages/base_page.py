class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False