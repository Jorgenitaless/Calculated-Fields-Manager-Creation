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

#Tiempos inicio
inicio = time.time()
#Inicializaciones
related = []
counter = 0
G = nx.DiGraph() 
#Lectura archivo
df = pd.read_csv('list.csv')
#Variables
longi =len(df)-1

#Lista BOs cargados
a_file = open("items.txt", "r")
lines = a_file.read()
items = lines.splitlines()
a_file.close()
#Lista BOs Vacíos
a_file = open("vacios.txt", "r")
lines = a_file.read()
vacios = lines.splitlines()
a_file.close()

#Carga de archivos para escritura
fileItems = open('items.txt','a')
fileVacios = open('vacios.txt','a')

#Carga de grafo si existe
if (os.path.exists('parts.gpickle')):
    G = nx.read_gpickle('parts.gpickle')
#Impresión de BOs faltantes
print("Cantidad de BOs Faltantes: %s" % (len(df) - len(items)))

while counter != longi:
    driver = webdriver.Chrome()
    action = ActionChains(driver)

    ft.start(driver)
    ft.login(driver)
    #Cada 300 termina sesión y vuelve a empezar
    for objeto in range(300):
        #si el objeto no ha sido cargado
        if df.iloc[counter, 0] not in items:
            #si el objeto no es vacío
            if df.iloc[counter, 0] not in vacios:
                related.clear()
                ft.search(df.iloc[counter, 1],driver, action, df.iloc[counter, 0])
                ft.guardarRBO(driver, related, df.iloc[counter, 0], action)
                ft.close(driver, action)
                #Escribir BOs procesado
                fileItems.write(df.iloc[counter, 0]+"\n")
                #Añador nodo a grafo
                G.add_node(df.iloc[counter, 0])
                #Si el BOs tiene RBOs
                if len(related) > 0:    
                    for item in related:
                        #Evitar duplicados y vacíos
                        if item not in related or item != '':
                                #Agregar relación
                                G.add_edge(df.iloc[counter, 0], item)
                else:
                    #Guardar BO vacío
                    fileVacios.write(df.iloc[counter, 0]+"\n")      
                 #Guardar grafo   
                pickle.dump(G, open('parts.gpickle', 'wb'))
                print("Completo relaciones de: %s" % df.iloc[counter, 0])
        counter = counter + 1
    driver.close()
    driver.quit()

file.close()
fin = time.time()
print(fin-inicio)

        




