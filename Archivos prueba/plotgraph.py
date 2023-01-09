import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['Worker', 'Job', 'Candidate', 'Class'])
G.add_weighted_edges_from([('Worker', 'Job', 1), ('Job', 'Candidate', 1), ('Candidate', 'Worker', 1), ('Class', 'Job', 1)])

#grafico
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()