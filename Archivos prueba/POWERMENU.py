import pandas as pd
import warnings
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException, TimeoutException)
import SelAut as aut
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
from pathlib import Path
import numpy as np
import mergefiles as mfiles

#inicia web driver
driver = webdriver.Chrome()
action = ActionChains(driver)

aut.start(driver)
aut.login(driver)

#Lista BOs cargados
a_file = open("items.txt", "r")
lines = a_file.read()
items = lines.splitlines()
a_file.close()

#Carga de archivos para escritura
fileItems = open('items.txt','a')

df = pd.read_csv('list.csv')

    
for wid, bo in zip(df['Workday ID'], df['Business Object']):
    aut.busqueda(wid, driver, action, bo)      
    aut.Excl(driver)
    aut.Btn(driver)
    aut.gotohome(driver)

    print("Completo relaciones de: " + bo)
    fileItems.write(bo + "\n")
  
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