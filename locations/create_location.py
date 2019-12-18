from selenium import webdriver

from pages.create_location_page import CreateLocationPage
from pages.list_locations_page import ListLocationsPage

driver = webdriver.Chrome()

list_page = ListLocationsPage(driver)
list_page.go()
list_page.assert_title_is_ok()
list_page.assert_table_contains_location("Budapest", "47.497912, 19.040235")
list_page.assert_count_of_table_rows_is(7)
list_page.click_to_create_location_link()

create_location = CreateLocationPage(driver)
create_location.fill_create_location_form("Almafalva", "1.2,12.23")
create_location.click_to_create_button()

list_page.go()
list_page.assert_count_of_table_rows_is(8)