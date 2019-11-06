from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://almamaka.github.io/first-project/")
#driver.find_element(By.NAME, "a").send_keys("6")

first_number = input("Adj meg egy számot! ")
second_number = input("Mivel adjam össze? ")

first_input_field = driver.find_element(By.NAME, "a")
first_input_field.send_keys(first_number)
#first_input_field.screenshot("first-input.png")

#driver.find_element(By.NAME, "b").send_keys("5")
second_input_field = driver.find_element(By.NAME, "b")
second_input_field.send_keys(second_number)

driver.find_element(By.NAME, "gomb1").click()
result = driver.find_element_by_id("result-input").get_attribute("value")
print(result)

driver.save_screenshot("result.png")

expected = int(first_number) + int(second_number)
print(expected)
print(result)

print(type(expected))
print(type(result))

assert int(result) == expected

header_text = driver.find_element(By.XPATH, "//h1").text
print(header_text)
assert header_text == "Calc"

driver.close()

