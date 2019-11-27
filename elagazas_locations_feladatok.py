import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.learnwebservices.com/locations/?size=100")


def location_lat_coord_is_greater_than_48(name):
    wait_xpath = "//tbody/tr"
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, wait_xpath))
    )

    xpath = "//tr[td[contains(text(), 'name')]]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

    lat = coords[0:coords.index(",")]
    print(lat)

    if float(lat) > 48:
        print("Szelesseg nagyobb mint 48!")


#irj egy fv-t, amely viszaadja név alapján a szélességi koordinátákat


def find_lat_from_name(find_name):
    wait_xpath = "//tbody/tr"
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, wait_xpath))
    )

    xpath = "//tr[td[contains(text(), 'name')]]/td[3]".replace("name", find_name)
    coords = driver.find_element(By.XPATH, xpath).text
    lat = coords[0:coords.index(",")]
    print(lat)
    return lat


def print_when_lat_greater_than_48(name):
    lat = find_lat_from_name(name)

    if float(lat) > 48:
        print("Szelesseg nagyobb mint 48!")



def print_when_lat_kisebb_mint_48(name):
    lat = find_lat_from_name(name)

    if float(lat) < 48:
        print("Szelesseg kisebb mint 48!")


#location_lat_coord_is_greater_than_48("fityiszváros")
find_lat_from_name("fityiszváros")
print_when_lat_kisebb_mint_48("fityiszváros")

