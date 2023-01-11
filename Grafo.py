import networkx as nx
import pickle
import matplotlib.pyplot as plt
import Functions as ft

G = nx.read_gpickle('parts.pickle')

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)

print(nx.shortest_path(G, source='Class', target='Functional Area'))
plt.show()

