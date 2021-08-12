import networkx as nx
import numpy as np

fp = r'C:\Users\anime\PycharmProjects\PyDSA\courseraStanford\DivideAndConquer\week4\kargerMinCut.txt'
graph = {}
G = nx.Graph()
np_arr = np.zeros((200, 200))
with open(fp, "r") as f:
    for line in f:
        info = line.rstrip().split("\t")
        vertex = int(info[0])
        connections = np.sort([int(x) for x in info[1:]])
        graph[vertex] = connections
        for c in connections:
            G.add_edge(vertex, c, capacity=1.0)

mc_list = []
for source in range(1, 199):
    mcs = [ nx.minimum_cut_value(G, source, target) for target in range(source + 1, 200)]
    print("For {} node as source min cut is {} for target {}".format(source, min(mcs), mcs.index(min(mcs))))

print(min(mc_list))
