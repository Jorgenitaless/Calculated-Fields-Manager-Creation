#Librerías
import pandas as pd
import json

def list_creation(business_objects):
    df = pd.read_csv('list.csv')

    for bo in df['Workday ID']:
        business_objects.append(bo)

