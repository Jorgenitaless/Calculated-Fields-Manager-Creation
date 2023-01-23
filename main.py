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

print("Cantidad de BOs: %s \nNumero en loop: %s" % (len(df),longi))

while counter != longi:
    driver = webdriver.Chrome()
    action = ActionChains(driver)

    ft.start(driver)
    ft.login(driver)

    for objeto in range(300):
        related.clear()
        ft.search(df.iloc[counter, 1],driver, action, df.iloc[counter, 0])
        ft.guardarRBO(driver, related, df.iloc[counter, 0], action)
        ft.close(driver, action)
        G.add_node(df.iloc[counter, 0])
        if len(related) > 0:    
            for item in related:
                if item not in related or item != '':
                    G.add_edge(df.iloc[counter, 0], item)
                
        pickle.dump(G, open('parts.pickle', 'wb'))
        print("Completo relaciones de: %s" % df.iloc[counter, 0])
        counter = counter + 1
    
    driver.close()
    driver.quit()

fin = time.time()
print(fin-inicio)

pickle.dump(G, open('graph.pickle', 'wb'))

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()
        




