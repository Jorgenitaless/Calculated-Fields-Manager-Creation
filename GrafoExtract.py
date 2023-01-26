########Librerías
import time
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
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException, TimeoutException)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle


inicio = time.time()
related = []
df = pd.read_csv('list.csv')
G = nx.DiGraph() #or G = nx.MultiDiGraph()
longi =len(df)-1
counter = 0

a_file = open("items.txt", "r")
lines = a_file.read()
items = lines.splitlines()
a_file.close()
print(items)

a_file = open("vacios.txt", "r")
lines = a_file.read()
vacios = lines.splitlines()
a_file.close()


fileItems = open('items.txt','a')
fileVacios = open('vacios.txt','a')

if (os.path.exists('parts.gpickle')):
    G = nx.read_gpickle('parts.gpickle')

print("Cantidad de BOs Faltantes: %s" % (len(df) - len(items)))

while counter != longi:
    driver = webdriver.Chrome()
    action = ActionChains(driver)

    ft.start(driver)
    ft.login(driver)

    for objeto in range(300):
        if df.iloc[counter, 0] not in items:
            if df.iloc[counter, 0] not in vacios:
                related.clear()
                ft.search(df.iloc[counter, 1],driver, action, df.iloc[counter, 0])
                ft.guardarRBO(driver, related, df.iloc[counter, 0], action)
                ft.close(driver, action)
                fileItems.write(df.iloc[counter, 0]+"\n")

                G.add_node(df.iloc[counter, 0])
                if len(related) > 0:    
                    for item in related:
                        if item not in related or item != '':
                                G.add_edge(df.iloc[counter, 0], item)
                else:
                    fileVacios.write(df.iloc[counter, 0]+"\n")      
                    
                pickle.dump(G, open('parts.gpickle', 'wb'))
                print("Completo relaciones de: %s" % df.iloc[counter, 0])
        counter = counter + 1
         
    
    driver.close()
    driver.quit()

file.close()
fin = time.time()
print(fin-inicio)

        




