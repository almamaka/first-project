from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://almamaka.github.io/first-project/")
driver.find_element(By.ID, "a").send_keys("6")
driver.find_element(By.ID, "b").send_keys("5")
driver.find_element(By.ID, "gomb1").click()


