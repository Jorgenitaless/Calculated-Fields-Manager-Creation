#Librerías
import pandas as pd
import os
import shutil
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import matplotlib.pyplot as plt
import networkx as nx
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException, TimeoutException)


#################### Selenium functions
def start(driver):
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://impl.workday.com/bnb_dpt1/d/pex/home.htmld?")

def login(driver):
    username = driver.find_element(By.XPATH,"//input[@class='gwt-TextBox GDPVGE1BM2B']")
    username.send_keys("wd-implementer")
    
    password = driver.find_element(By.XPATH,"//input[@class='gwt-PasswordTextBox GDPVGE1BM2B']")
    password.send_keys("!l0v3WDAY")
    
    login = driver.find_element(By.XPATH, "//button[@data-automation-id='goButton']")
    login.click()  
   
def search(tarea, driver, action, nombre):
    busquedaGlobal = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']"))
    )
    action.click(on_element = busquedaGlobal)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    task = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="'+nombre+'"]'))
    )
    task.click()

def close(driver, action):
    try:
        close = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-automation-id= 'searchInputClearTextIcon']"))
        )
    except(TimeoutException):
        close = driver.find_element(By.XPATH, "//span[@class= 'css-9gpxd9']")
        
    action.click(on_element = close)
    action.perform() 

def guardarRBO(driver, classBO, bo, action):
    element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id = 'tableWrapper']"))
        ) 
    
    try: 
        campos = driver.find_elements(By.XPATH, "//tr/td[5]")
        if len(campos) > 0:
            selector = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-automation-id = 'excelIconButton']")))
            selector.click()
            downloadBtn = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-automation-id = 'uic_downloadButton']")))                #acciones complicadas con el mouse 
            action.move_to_element(downloadBtn)
            action.click(downloadBtn)
            action.perform()
        
    
    except (NoSuchElementException,TimeoutException):
        print("No hay valores") 
    


    
    