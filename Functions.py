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
            EC.visibility_of_element_located((By.XPATH, "//span[@class= 'css-9gpxd9']"))
        )
    except(TimeoutException):
        close = driver.find_element(By.XPATH, "//span[@class= 'css-9gpxd9']")
    action.move_to_element(close).click(on_element = close)
    action.perform() 

def guardarRBO(driver, classBO, bo, action):
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


def program(G):
    print("BO inicio")
    source = input()
    print("BO Objetivo")
    target = input()
    print(nx.shortest_path(G, source=source, target=target))
    
