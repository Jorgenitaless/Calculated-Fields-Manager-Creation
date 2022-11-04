#Librerías
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#################### List creation
def list_creation(business_objects):
    df = pd.read_csv('list.csv')

    for bo in df['Workday ID']:
        business_objects.append(bo)

#################### Selenium functions
def start(driver):
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://impl.workday.com/bnb_dpt1/d/pex/home.htmld?")



def login(driver):
    username = driver.find_element(By.CSS_SELECTOR, 'input.gwt-TextBox.GDPVGE1BM2B')
    username.send_keys("wd-implementer")

    password = driver.find_element(By.CSS_SELECTOR, 'input.gwt-PasswordTextBox.GDPVGE1BM2B')
    password.send_keys("!l0v3WDAY")

    login = driver.find_element(By.XPATH, "//div[@class = 'GDPVGE1BLTC']/button")
    login.click()
    
def search(tarea, driver):
    driver.implicitly_wait(20)
    search = driver.find_element(By.XPATH, "//div[@id = 'wd-searchInput']/input")

    driver.implicitly_wait(20)
    action = ActionChains(driver)
    action.click(on_element = search)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    driver.implicitly_wait(20)
    task = driver.find_element(By.XPATH, "//a[text()='"+tarea+"']")
    task.click()
