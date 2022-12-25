########Librerías
import sys
import os
import Functions as ft
from selenium import webdriver
import networkx as nx
import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException)

driver = webdriver.Chrome()
counter = 0

related = []
df = pd.read_csv('list.csv')
G = nx.DiGraph() #or G = nx.MultiDiGraph()

ft.start(driver)
ft.login(driver)
longi =len(df)-1

try:
    for objeto in range(longi):
        print(counter)
        if counter == 0:
            try:
                driver.implicitly_wait(10)
                ft.search('Business Object Details',driver)
                driver.implicitly_wait(10)
                ft.BODetails(df.iloc[counter, 1], driver)
                driver.implicitly_wait(10)
                ft.submit(driver)
            except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
                
                driver.implicitly_wait(10)
                ft.cancel(driver)
                driver.implicitly_wait(10)
                tarea = "bo:" + df.iloc[counter, 0]
                busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
                driver.implicitly_wait(10)
                action = ActionChains(driver)
                action.click(on_element = busquedaGlobal)
                driver.implicitly_wait(10)
                action.send_keys(tarea)
                action.send_keys(Keys.RETURN)
                action.perform()
                
                driver.implicitly_wait(20)
                
                task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
                driver.implicitly_wait(10)
                task.click()
                driver.implicitly_wait(10)
                ft.guardarRBO(driver, related)
                driver.implicitly_wait(10)
                G.add_node(df.iloc[counter, 0])
                for item in related:
                    G.add_edge(df.iloc[counter, 0], item)
                print("No campo")
            driver.implicitly_wait(10)
            ft.guardarRBO(driver, related)
            G.add_node(df.iloc[counter, 0])
            
            for item in related:
                G.add_edge(df.iloc[counter, 0], item)
            print(df.iloc[counter, 0])
            counter = counter + 1
            
        if counter > 0:
            related.clear()
            driver.implicitly_wait(10)
            ft.close(driver)
            driver.implicitly_wait(10)
            try:
                ft.search('Business Object Details',driver)
                driver.implicitly_wait(10)
                ft.BODetails(df.iloc[counter, 1], driver)
                driver.implicitly_wait(10)
                ft.submit(driver)
            except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
                
                driver.implicitly_wait(10)
                ft.cancel(driver)
                driver.implicitly_wait(10)
                tarea = "bo:" + df.iloc[counter, 0]
                busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
                driver.implicitly_wait(10)
                action = ActionChains(driver)
                action.click(on_element = busquedaGlobal)
                driver.implicitly_wait(10)
                action.send_keys(tarea)
                action.send_keys(Keys.RETURN)
                driver.implicitly_wait(10)
                action.perform()
                
                driver.implicitly_wait(20)
                
                task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
                task.click()
                ft.guardarRBO(driver, related)
                
                driver.implicitly_wait(10)
                
                G.add_node(df.iloc[counter, 0])
                
                for item in related:
                    G.add_edge(df.iloc[counter, 0], item)
                    
                print("No campo")
                
            driver.implicitly_wait(10)
            ft.guardarRBO(driver, related)
            
            driver.implicitly_wait(10)
            
            G.add_node(df.iloc[counter, 0])
            
            for item in related:
                G.add_edge(df.iloc[counter, 0], item)
            
            print(df.iloc[counter, 0])
            counter = counter + 1
except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
    
    driver.implicitly_wait(10)
    ft.cancel(driver)
    driver.implicitly_wait(10)
    tarea = "bo:" + df.iloc[counter, 0]
    busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
    action = ActionChains(driver)
    action.click(on_element = busquedaGlobal)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    
    driver.implicitly_wait(20)
    
    task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
    task.click()
    ft.guardarRBO(driver, related)
    driver.implicitly_wait(10)
    G.add_node(df.iloc[counter, 0])
    for item in related:
        G.add_edge(df.iloc[counter, 0], item)
        print(df.iloc[counter, 0])
    print("No element")

print("Final")       
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()
        




