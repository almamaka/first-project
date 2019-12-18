from selenium import webdriver

from db.db_operations import DbOperation
from pages.create_location_page import CreateLocationPage
from pages.details_page import LocationsDetailsPage
from pages.list_locations_page import ListLocationsPage

driver = webdriver.Chrome()

db_operations = DbOperation()
db_operations.delete_locations()

list_page = ListLocationsPage(driver)
list_page.go()
list_page.assert_title_is_ok()
list_page.assert_count_of_table_rows_is(0)
list_page.click_to_create_location_link()

create_location = CreateLocationPage(driver)
create_location.fill_create_location_form()
create_location.click_to_create_button()

details_page = LocationsDetailsPage(driver)
details_page.click_to_back_to_list_link()
list_page.assert_table_contains_location("Almafalva", "1, 1")
list_page.assert_count_of_table_rows_is(1)