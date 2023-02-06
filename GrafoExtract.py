########Librerías
import time
import sys
import os
import shutil
import glob
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
    for objeto in range(1000):
        related.clear()
        #si el objeto no ha sido cargado
        if df.iloc[counter, 0] not in items:
            #si el objeto no es vacío
            if df.iloc[counter, 0] not in vacios:
                ft.search(df.iloc[counter, 1],driver, action, df.iloc[counter, 0])
                ft.guardarRBO(driver, related, df.iloc[counter, 0], action)
                ft.close(driver, action)
                #Escribir BOs procesado
                fileItems.write(df.iloc[counter, 0]+"\n")
                #Añador nodo a grafo
                G.add_node(df.iloc[counter, 0])
                
                #file = df.iloc[counter, 0].replace(" ", "_") + '.xlsx'
                excel_files = glob.glob('/Users/claudiasoria/Downloads/*.xlsx')
                destino = os.getcwd() +'/Excels'
                for excel in excel_files:
                    rbos = pd.read_excel(excel, engine="openpyxl", skiprows=[0])
                    rbos.dropna()
                    related = list(rbos.iloc[:, 4].dropna())
                    name = os.path.basename(excel)
                    direc = '/Users/claudiasoria/Downloads/' + name
                    print(direc)
                    shutil.move(direc, destino)
                    
                
                #Si el BOs tiene RBOs
                if len(related) > 0:  
                    for item in related:
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
#Tiempo final
fin = time.time()
print(fin-inicio)

'''
#find files
path = "/Users/claudiasoria/Downloads"
destpath = "/Users/claudiasoria/Downloads/BO_files/"
directory = "BO_files"
pattern = "\*.xlsx"

try:
    newdirect = os.path.join(path, directory)
    os.mkdir(newdirect)
except FileExistsError:
    pass

files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.xlsx')]

for file in files:
    file_name = os.path.basename(file)
    new_path = destpath + file_name
    shutil.move(file, new_path)
    
origin = "/Users/karlabarajas/Downloads/BO_files/"
target = "/Users/karlabarajas/Documents/CF-Manager/BO_files/"
files = os.listdir(origin)

for file in files:
    shutil.move(origin + file,target)
    print(file)

excel_files = glob.glob('/Users/karlabarajas/Documents/CF-Manager/BO_files/*.xlsx') # assume the path
for excel in excel_files:
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data = pd.read_excel (excel, engine="openpyxl", skiprows=[0])
        newbo = Path(excel).stem
        data.insert(0, "Weight", 1)
        data.insert(1, "Business Object", newbo)
        data['Related Business Object'].replace('', np.nan, inplace=True)
        data['Related Business Object'].replace(newbo, np.nan, inplace=True) #podría fallar ya que simplemente quita esa palabra de la linea
        data.dropna(subset=['Related Business Object'], inplace=True)
        data.drop(['Description', 'Field Source', 'Field Name', 'Field Type', 'Built-in Prompts', 'Category', 'Authorized Usage'], axis=1, inplace = True)

        out = excel.split('.')[0]+'.csv'
        data.to_csv(out)


filepath = "/Users/karlabarajas/Documents/CF-Manager/BO_files"
mfiles.mergeinfo(filepath)

 '''       




