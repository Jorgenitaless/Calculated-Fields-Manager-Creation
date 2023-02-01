import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException, TimeoutException)


def busqueda(tarea, driver, action, nombre):
    busquedaGlobal = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']")))
    action = ActionChains(driver)
    action.click(on_element = busquedaGlobal)

    action.send_keys(tarea)
    driver.implicitly_wait(10)
    action.send_keys(Keys.RETURN)
    action.perform()

    task = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='"+nombre+"']")))
    task.click()

def start(driver):
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(20)
    driver.get("https://impl.workday.com/bnb_dpt1/d/pex/home.htmld?")


def login(driver):
    username = driver.find_element(By.CSS_SELECTOR, 'input.gwt-TextBox.GDPVGE1BM2B')
    username.send_keys("wd-implementer")

    password = driver.find_element(By.CSS_SELECTOR, 'input.gwt-PasswordTextBox.GDPVGE1BM2B')
    password.send_keys("!l0v3WDAY")

    login = driver.find_element(By.XPATH, "//div[@class = 'GDPVGE1BLTC']/button")
    login.click() 

def findbo(bo, driver):
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, "//div[@class = 'css-1xms06i-ListContainer edt0qdt8']")
    action = ActionChains(driver)
    selec = driver.find_element(By.XPATH, "//div[text()='"+bo+"']")
    selec.click()
    action.send_keys(Keys.RETURN)
    action.perform()
    
def Btn(driver):
    try:
        downloadBtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'WJGN WNGN WISO WJ-N WAIN']")))
        action = ActionChains(driver)                 #acciones complicadas con el mouse 
        action.move_to_element(downloadBtn)
        action.click(downloadBtn)
        action.perform()
    except(TimeoutException,NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
        driver.implicitly_wait(60)
        downloadBtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'WJGN WISO WJ-N WAIN WNGN']")))
        action = ActionChains(driver)                 #acciones complicadas con el mouse class="WJGN WISO WJ-N WAIN WNGN"
        action.move_to_element(downloadBtn)
        action.click(downloadBtn)
        action.perform()

def Excl(driver):
    selector = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'WJ3K WI3K WA2K WE2K WC2K WISO']")))
    selector.click()
    driver.implicitly_wait(20)

def gotohome(driver):
    home = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'wdappchrome-q']")))
    #home = driver.find_element(By.XPATH, "//button[@class = 'wdappchrome-q']")
    home.click()
    driver.implicitly_wait(20)

def cancl(driver): 
    resetact = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'WJGN WNGN WISO WJ-N WGFN']")))
    action = ActionChains(driver)                 #acciones complicadas con el mouse 
    action.click(on_element = resetact)
    action.perform()
    resetact.click()

def close(driver):
    close = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class= 'css-9gpxd9']")))
    action = ActionChains(driver)                 #acciones complicadas con el mouse 
    action.click(on_element = close)
    action.perform() 