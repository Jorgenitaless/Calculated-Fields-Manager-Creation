
import matplotlib.pyplot as plt
import networkx as nx
import pickle

#graph = {'Worker':{'Supervisory':1,'c':1},'Supervisory':{'Worker':1,'c':1,'d':1},'c':{'Supervisory':1,'d':1,'e':1},'d':{'c':1,'e':1},'e':{'d':1},'f':{'d':1}}
graph = nx.read_gpickle('graph.pickle')

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('The path is ' + str(path))
 
 
dijkstra(graph, 'Class', 'Instance')