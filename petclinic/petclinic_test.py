from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost:8080/")


def assert_title_is(title):
    assert driver.title == title
    print(title)


def assert_header_is(titleh):
    header_title = driver.find_element(By.XPATH, "//div[@class = 'container xd-container']/h2").text
    assert header_title == titleh
    print(header_title)


def assert_image_is_present(image):
    s = image
    if len(s) > 0:
        driver.find_element(By.XPATH, "//div[@class = 'col-md-12']/img[contains(text(), image)]")
        print("A kép megtalálható az oldalon.")


def test_home_page(title, titleh, image):
    assert_title_is(title)
    assert_header_is(titleh)
    assert_image_is_present(image)
    print("Minden jól jelenik meg a kezdőoldalon.")


test_home_page(driver.title, "Welcome", "img")
#assert_title_is(driver.title)
#assert_header_is("Welcome")
#assert_image_is_present("img")
driver.close()

