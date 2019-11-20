from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def print_welcome():
    print("Kezdodhet a teszteles!")


print_welcome()

# olyan fvt, ami ráklikkel a beviteli mezőre, click_to_name_input() legyen a neve
# írj egy oylan fvt, ami a paraméterként kapott nevet beírja beviteli mezőbe, type_to_name_input()
# majd írj egy olyan fvt, ami ráklikkel a címsorra, click_to_header()
# írj egy fvt, mely paraméterként megadott hibaüzenetre vár, wait_for_error_message()
# olvassa be a monogramot, és azzal térjen vissza, read_monogram()
driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")


def click_to_name_input():
    driver.find_element(By.ID, 'create-form:name-input').click()


def type_to_name_input(name):
    driver.find_element(By.ID, "create-form:name-input").send_keys(name)


def click_to_header():
    driver.find_element(By.XPATH, '//html/body/div/h1').click()

def wait_for_error_message(hibauzenet):
    # driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text

    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"),
                                                          hibauzenet))
    return hibauzenet


def print_hibauzenet():
    hibauzi = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
    print(hibauzi)


def wait_for_monogram(expected_monogram):
    WebDriverWait(driver, 3).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'create-form:monogram-text'),
                                                expected_monogram)
    )

    return driver.find_element(By.ID, 'create-form:monogram-text').text


click_to_name_input()
click_to_header()
wait_for_error_message('Az alkalmazott nevét meg kell adni!')
print_hibauzenet()
click_to_name_input()
type_to_name_input('Alma')
# monogram = read_monogram()
print(wait_for_monogram('A'))

# valamit átírok benne mert ezahülyenemküldifel

#print(hibauzenet)


