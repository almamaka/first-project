from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com//locations/server")
koord = driver.find_element(By.XPATH, "//tr[td[text() = 'Dobogókő']]/td[3]").text
print (koord)
print(type(koord))

melyik_varos = driver.find_element(By.XPATH, "//tr[td[text() = '9147']]/td[2]").text
print(melyik_varos)
print(type(melyik_varos))