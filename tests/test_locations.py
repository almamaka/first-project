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
        self.create_location_page = CreateLocationPage(self.driver)
        self.details_page = LocationsDetailsPage(self.driver)

    def teardown_method(self):
        self.driver.close()

    def test_empty_table(self):
        self.list_page.go()
        self.list_page.assert_title_is_ok()
        self.list_page.assert_count_of_table_rows_is(20)

    def test_when_create_location_then_details_are_correct(self):
        self.create_location()

        self.details_page.assert_details_are("Budapest", "1.0, 1.0")
        self.details_page.assert_message_has_been_appeared("Location has been created.")

    def test_when_create_location_then_appears_in_the_table(self):
        self.create_location()

        self.details_page.click_to_back_to_list_link()
        self.list_page.assert_table_contains_location("Budapest", "1.0, 1.0")

    def test_when_create_20_locations_then_appears_in_the_table(self):
        with open("../locations_cities.csv", encoding="UTF-8") as file:
            for line in file:
                print(line.strip())
                (name, lat, lon) = line.strip().split(",")
                self.create_location(name, f"{lat},{lon}")
        self.list_page.go()
        self.list_page.assert_count_of_table_rows_is(20)

    def create_location(self, name="Budapest", coords="1,1"):
        self.list_page.go()
        self.list_page.click_to_create_location_link()
        self.create_location_page.fill_create_location_form(name, coords)
        self.create_location_page.click_to_create_button()
