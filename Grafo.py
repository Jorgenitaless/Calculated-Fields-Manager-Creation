import networkx as nx
import pickle
import matplotlib.pyplot as plt
import Functions as ft



pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)

print(nx.shortest_path(G, source='Worker', target='First Name'))
#plt.show()

