import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Combined_files.csv")
G = nx.from_pandas_edgelist(df, source='Business Object', target='Related Business Object', edge_attr='Weight', create_using=nx.DiGraph())

#Grafico
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'Weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

rBO = input('Introduce el rBO: ')
BOp = input('Introduce el BO: ')

shortest_value = nx.shortest_path_length(G, source=rBO, target=BOp)
print(shortest_value)
shortest_path = nx.shortest_path(G, source=rBO, target=BOp, method='dijkstra')
print('shortest path：{}'.format(shortest_path))
print('distance：{}'.format(shortest_value))