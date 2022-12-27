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
        EC.presence_of_element_located((By.XPATH, "//input[@data-automation-id='globalSearchInput']"))
    )
    #busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
    action = ActionChains(driver)
    action.click(on_element = busquedaGlobal)
    action.send_keys(tarea)
    driver.implicitly_wait(10)
    action.send_keys(Keys.RETURN)
    action.perform()
    task = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='"+tarea+"']"))
    )
    #task = driver.find_element(By.XPATH, "//a[text()='"+tarea+"']")
    task.click()
    
def BODetails(bo, driver):
    busquedaBO = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-automation-id='responsiveMonikerInput']"))
    )
    #busquedaBO = driver.find_element(By.XPATH, "//div[@data-automation-id='responsiveMonikerInput']")
    action = ActionChains(driver)
    action.click(on_element = busquedaBO)
    action.send_keys(bo)
    driver.implicitly_wait(10)
    action.send_keys(Keys.ENTER)
    action.perform()


def close(driver):
    close = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-automation-id = 'searchInputClearTextIcon']"))
    ).click()
    #close = driver.find_element(By.XPATH, "//button[@data-automation-id = 'searchInputClearTextIcon']")
    #action = ActionChains(driver)
    #action.click(on_element = close)
    #action.perform() 
    

def submit(driver):
    OkButton = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']"))
    )
    #OkButton = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WAIN']")
    action = ActionChains(driver)
    action.click(on_element = OkButton)
    action.perform()
    OkButton.click()
    
def cancel(driver):
    cancel = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WGFN']"))
    )
    #cancel = driver.find_element(By.XPATH, "//button[@class='WJGN WNGN WISO WJ-N WGFN']")
    action = ActionChains(driver)
    action.click(on_element = cancel)
    action.perform()
    cancel.click()


def guardarRBO(driver, classBO):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tr/td[5]"))
    )
    campos = driver.find_elements(By.XPATH, "//tr/td[5]")
    for campo in campos:
        classBO.append(campo.text)


#################### Search Algorithm
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('The path is ' + str(path))
        
