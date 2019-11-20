from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def print_welcome():
    print("Kezdodhet a teszteles!")


print_welcome()

# irj fvt, ami ráklikkel a create employee gombra
# irj fvt, ami kitolti a kartyaszamot
# irj fvt, ami ráklikkel a második employee gombra

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee-details.xhtml")

def click_on_create_employee_button():
    driver.find_element(By.ID, 'create-form:save-button').click()


def print_hibauzenet():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//html/body/div/ul/li"),
                                                          'Card number is already used'))
    hibauzenet = driver.find_element(By.ID, "//html/body/div/ul/li").text
    print(hibauzenet)


def type_code():
    driver.find_element(By.ID, '')


