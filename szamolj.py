from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://almamaka.github.io/first-project/")
#driver.find_element(By.NAME, "a").send_keys("6")

first_input_field = driver.find_element(By.NAME, "a")
first_input_field.send_keys("6")
first_input_field.screenshot("first-input.png")

driver.find_element(By.NAME, "b").send_keys("5")

driver.find_element(By.NAME, "gomb1").click()
result = driver.find_element_by_id("result-input").get_attribute("value")
print(result)

driver.save_screenshot("result.png")

assert result == "11"

header_text = driver.find_element(By.XPATH, "//h1").text
print(header_text)
assert header_text == "Calc"

driver.close()

