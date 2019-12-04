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
        print("This image is present.")


def test_home_page(title, titleh, image):
    assert_title_is(title)
    assert_header_is(titleh)
    assert_image_is_present(image)
    print("Every expected element is present on the page.")


def goto_home_page():
    driver.find_element(By.XPATH, "//span[text() = 'Home']").click()
    print("Start page opened")


def goto_find_owners():
    driver.find_element(By.XPATH, "//span[text() = 'Find owners']").click()
    print("Find owners page opened")


def goto_veterinarians():
    driver.find_element(By.XPATH, "//a[@href = '/vets.html']").click()
    print("Veterinarians page opened")


def find_find_owners_header():
    owner_header = driver.find_element(By.XPATH, "//div[@class = 'container xd-container']/h2[text() = 'Find Owners']").text
    print(owner_header)


def find_last_name_label_on_find_owner_page():
    driver.find_element(By.XPATH, "//label[contains(text(), 'Last name')]")
    print("Last name label is there")


def find_last_name_input_on_find_owner_page():
    driver.find_element(By.XPATH, "//input[@class = 'form-control']")
    print("Last name input is present")


def test_find_owners_page():
    goto_find_owners()
    find_find_owners_header()
    find_last_name_label_on_find_owner_page()
    find_last_name_input_on_find_owner_page()


test_home_page(driver.title, "Welcome", "img")
#assert_title_is(driver.title)
#assert_header_is("Welcome")
#assert_image_is_present("img")


goto_find_owners()
goto_veterinarians()
goto_home_page()


test_find_owners_page()
#find_last_name_label_on_find_owner_page()
#driver.close()

