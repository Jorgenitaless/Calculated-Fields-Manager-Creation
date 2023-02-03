import os
import shutil
import pandas as pd

df = pd.read_excel('Excels/Class.xlsx')
classBO = list(df.iloc[:, 4])

print(classBO[6])