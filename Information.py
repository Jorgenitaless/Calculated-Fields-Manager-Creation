
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://impl.workday.com/bnb_dpt1/d/pex/home.htmld?")

classBO = []



driver.implicitly_wait(20)
username = driver.find_element(By.XPATH,"//input[@class='gwt-TextBox GDPVGE1BM2B']")
username.send_keys("wd-implementer")
password = driver.find_element(By.XPATH,"//input[@class='gwt-PasswordTextBox GDPVGE1BM2B']")
password.send_keys("!l0v3WDAY")
login = driver.find_element(By.XPATH, "//button[@data-automation-id='goButton']")
login.click()

busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
action = ActionChains(driver)
action.click(on_element = busquedaGlobal)
action.send_keys("Business Object Details")
action.send_keys(Keys.RETURN)
action.perform()
driver.implicitly_wait(20)
task = driver.find_element(By.XPATH, "//a[text()='Business Object Details']")
task.click()

driver.implicitly_wait(20)
busquedaBO = driver.find_element(By.XPATH, "//div[@data-automation-id='responsiveMonikerInput']")
action = ActionChains(driver)
action.click(on_element = busquedaBO)
action.send_keys("3cf87e1fc91f41689cdbee7064985015")
action.send_keys(Keys.ENTER)
action.perform()

OkButton = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']")
action = ActionChains(driver)
action.click(on_element = OkButton)
action.perform()
OkButton.click()

cancel = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WGFN']")
action = ActionChains(driver)
action.click(on_element = cancel)
action.perform()
cancel.click()
'''
OkButton = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']")
action = ActionChains(driver)
action.click(on_element = OkButton)
action.perform()
OkButton.click()

campos = driver.find_elements(By.XPATH, "//tr/td[5]")

for campo in campos:
    classBO.append(campo.text)

print(classBO)

driver.implicitly_wait(10)
close = driver.find_element(By.XPATH, "//button[@data-automation-id = 'searchInputClearTextIcon']")
action = ActionChains(driver)
action.click(on_element = close)
action.perform() 
driver.implicitly_wait(10)
action.send_keys(bo)

'''







