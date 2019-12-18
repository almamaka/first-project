from selenium.webdriver.chrome.webdriver import WebDriver


class LocationsDetailsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_to_back_to_list_link(self):
        self.driver.find_element_by_link_text("Back to list").click()