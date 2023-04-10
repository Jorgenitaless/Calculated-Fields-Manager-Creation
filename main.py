import networkx as nx
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import json
from pandas.io.json import json_normalize 

with open('BNB_Classes_Info.json','r') as f:
    d = json.loads(f.read())
    
df = pd.json_normalize(data = d['Report_Entry'], record_path= 'Report_Fields', meta= ['Business_Object_Name'])

data = df.loc[:, ['Business_Object_Name', 'RBO', 'Field']]
g_data = data.groupby(['Business_Object_Name', 'RBO'])['Field'].apply(', '.join).reset_index()

Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(g_data, source='Business_Object_Name', target='RBO', edge_attr='Field', create_using=nx.DiGraph())
pickle.dump(G, open('parts.gpickle', 'wb'))

