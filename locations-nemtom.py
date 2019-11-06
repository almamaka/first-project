from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#Chrome zárójelei közé az útvonalat is be lehet írni, ha nincs benne a környezeti változók között az elérési útvonal

driver.get("http://www.learnwebservices.com//locations/server")
driver.find_element(By.ID, "nameInput").send_keys("Selenium")

# driver.quit()