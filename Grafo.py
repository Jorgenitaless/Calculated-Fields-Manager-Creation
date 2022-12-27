import networkx as nx
import pickle
import matplotlib.pyplot as plt

G = nx.read_gpickle('graph.pickle')
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()