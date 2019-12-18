from selenium import webdriver

from db.db_operations import DbOperation
from pages.list_locations_page import ListLocationsPage


class TestLocations:

    def test_empty_table(self):
        driver = webdriver.Chrome()
        db_operations = DbOperation()
        db_operations.delete_locations()

        list_page = ListLocationsPage(driver)
        list_page.go()
        list_page.assert_title_is_ok()
        list_page.assert_count_of_table_rows_is(0)