from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.learnwebservices.com/locations/")


def click_on_create_location():
    driver.find_element(By.ID, "create-location-link").click()


def wait_for_name_input():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, "location-name")
        )
    )
    return driver.find_element(By.ID, "location-name")


def wait_for_coords_input():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, "location-coords")
        )
    )
    return driver.find_element(By.ID, "location-coords")


def type_location_name(location_name):
    driver.find_element(By.ID, "location-name").send_keys(location_name)


def type_coords(coord1, coord2):
    driver.find_element(By.ID, "location-coords").send_keys(coord1, ",", coord2)

def create_new_location():
    driver.find_element(By.XPATH, "//*[@id='location-form']/input[1]").click()




def find_new_location():
    found_location_name = driver.find_element(By.XPATH, "//table/tbody/tr[td[text() = location_name]]").text
    return found_location_name


def equal_to_new_location():
    if found_location_name == location_name:
        print('New location equals to found location!')
    else:
        print('Did not find new location!')


click_on_create_location()
type_location_name("Almafalva")
type_coords("55", "57.11")
create_new_location()
find_new_location()
equal_to_new_location()




