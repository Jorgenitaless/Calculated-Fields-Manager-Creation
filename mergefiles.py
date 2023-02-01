import pandas as pd
import os
import glob

def mergeinfo(file_path):
#file_path = "/Users/karlabarajas/Documents/CF-Manager/BO_files"
    file_list = os.chdir(file_path)

    csv_files = glob.glob('*.{}'.format('csv'))

    print(csv_files)

    #append all files together
    df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)

    #Exporting the file to your directory
    df_concat.to_csv('/Users/karlabarajas/Documents/CF-Manager/Combined_files.csv')