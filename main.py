import networkx as nx
import pickle
import matplotlib.pyplot as plt


G = nx.read_gpickle('parts.gpickle')
'''
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)

plt.show()


#ft.program(G)
print(list(G.nodes))
'''
print(nx.shortest_path(G, source='Worker', target = 'Dependent'))