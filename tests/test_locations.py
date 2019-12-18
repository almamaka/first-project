from selenium import webdriver

from db.db_operations import DbOperation
from pages.create_location_page import CreateLocationPage
from pages.details_page import LocationsDetailsPage
from pages.list_locations_page import ListLocationsPage


class TestLocations:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        db_operations = DbOperation()
        db_operations.delete_locations()
        self.list_page = ListLocationsPage(self.driver)
        self.create_location = CreateLocationPage(self.driver)
        self.details_page = LocationsDetailsPage(self.driver)

    def teardown_method(self):
        self.driver.close()

    def test_empty_table(self):
        self.list_page.go()
        self.list_page.assert_title_is_ok()
        self.list_page.assert_count_of_table_rows_is(0)

    def test_when_create_location_then_details_are_correct(self):
        self.list_page.go()
        self.list_page.click_to_create_location_link()

        self.create_location.fill_create_location_form("Budapest", "1,1")
        self.create_location.click_to_create_button()

        self.details_page.assert_details_are("Budapest", "1.0, 1.0")
        self.details_page.assert_message_has_been_appeared("Location has been created.")
