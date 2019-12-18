from selenium.webdriver.chrome.webdriver import WebDriver


class CreateLocationPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_create_location_form(self, name, coordinates):
        self.driver.find_element_by_id("name-input").send_keys(name)
        self.driver.find_element_by_id("coords-input").send_keys(coordinates)

    def click_to_create_button(self):
        self.driver.find_element_by_class_name("btn-primary").click()