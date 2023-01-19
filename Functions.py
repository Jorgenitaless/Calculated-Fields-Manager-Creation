#Librerías
import pandas as pd
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
    
def search(tarea, driver):
    busquedaGlobal = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']"))
    )
    #busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
    action = ActionChains(driver)
    action.click(on_element = busquedaGlobal)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    task = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='"+tarea+"']"))
    )
    #task = driver.find_element(By.XPATH, "//a[text()='"+tarea+"']")
    task.click()
    
def BODetails(bo, driver):
    try:
        busquedaBO = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id='responsiveMonikerInput']"))
        )
    except(TimeoutException):
        busquedaBO = driver.find_element(By.XPATH, "//div[@data-automation-id='responsiveMonikerInput']")
        
    action = ActionChains(driver)
    action.click(on_element = busquedaBO)
    action.send_keys(bo)
    action.send_keys(Keys.ENTER)
    action.perform()


def close(driver):
    try:
        close = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class= 'css-9gpxd9']"))
        )
    except(TimeoutException):
        close = driver.find_element(By.XPATH, "//span[@class= 'css-9gpxd9']")
    action = ActionChains(driver)
    action.click(on_element = close)
    action.perform() 
    

def submit(driver):
    OkButton = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']"))
    )
    #OkButton = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']")
    action = ActionChains(driver)
    action.click(on_element = OkButton)
    action.perform()
    OkButton.click()
    
def cancel(driver):
    try: 
        cancel = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WGFN']"))
        )
    except (TimeoutException):
        cancel = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WGFN']")
        
    action = ActionChains(driver)
    action.click(on_element = cancel)
    action.perform()
    cancel.click()


def guardarRBO(driver, classBO, bo):
    try: 
        popup = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id = 'errorWidgetInlineMessageTextCanvas']"))
            )
        
        print("Salta excepcion, Buscando por bo:Business object")
        cancel(driver)
        close(driver)
        tareaBO = "bo:" + bo
        busquedaGlobal = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']"))
        ).clear()
        action = ActionChains(driver)
        action.click(on_element = busquedaGlobal)
        action.send_keys(tareaBO)
        action.send_keys(Keys.RETURN)
        action.perform()
        task = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='"+bo+"']"))
        )
        task.click()
        
        guardarRBO(driver, classBO, bo)
        
    except(TimeoutException):
        element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id = 'tableWrapper']"))
        )
       
        
        
        try: 
            campos = driver.find_elements(By.XPATH, "//tr/td[5]")
        except (NoSuchElementException,TimeoutException):
            print("No hay valores")    
        if campos:
            for campo in campos:
                    classBO.append(campo.text)
    
    
    '''
    try:    
        element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id = 'tableWrapper']"))
        )
    except (TimeoutException): 
        print("Salta excepcion, Buscando por bo:Business object")
        cancel(driver)
        close(driver)
        tareaBO = "bo:" + bo
        busquedaGlobal = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']"))
        ).clear()
        action = ActionChains(driver)
        action.click(on_element = busquedaGlobal)
        action.send_keys(tareaBO)
        action.send_keys(Keys.RETURN)
        action.perform()
        task = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='"+bo+"']"))
        )
        task.click()
            
        guardarRBO(driver, classBO, bo)
           
    
    try: 
        campos = driver.find_elements(By.XPATH, "//tr/td[5]")
    except (NoSuchElementException,TimeoutException):
        print("No hay valores")
        
    if campos:
        for campo in campos:
                classBO.append(campo.text)
'''