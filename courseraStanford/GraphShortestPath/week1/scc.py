from collections import defaultdict, deque

import networkx as nx


def get_qn_graph():
    qn_graph = defaultdict(set)
    G = nx.DiGraph()

    with open("SCC.txt", "r") as f:
        for line in f.readlines():
            src, target = [int(x) for x in line.rstrip().split(" ") if x and len(x) > 0]
            qn_graph[src].add(target)
            G.add_edge(src, target)

    print(len(qn_graph))

    components = nx.strongly_connected_components(G)
    sorted_components = sorted(components, key=lambda x: len(x), reverse=True)
    print([len(x) for x in sorted_components[:5]])
    return qn_graph


class StronglyConnectedComponent:

    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.node_finish_time = dict()
        self.node_leader = dict()
        self.t = 0
        self.leader = 0
        self.nodes = range(1, len(graph) + 1)

    def find_scc(self):
        stack1 = deque()
        graph = self.graph
        for node in self.nodes[::-1]:
            if node not in self.visited:
                stack1.append(node)

                while len(stack1) > 0:
                    node_ = stack1.pop()
                    self.visited.add(node_)

                    for child in graph[node_]:
                        if child not in self.visited:
                            stack1.append(child)
                    
                    self.t += 1
                    self.node_finish_time[node] = self.t

        newGraph = self.create_new_graph()
        stack2 = deque()
        scc_count = {}
        self.visited = set()
        for node in self.nodes[::-1]:
            if node not in self.visited:
                stack2.append(node)
                self.leader = node
                len_leader = len(self.node_leader)
                while len(stack2) > 0:
                    node_ = stack2.pop()
                    self.visited.add(node_)
                    self.node_leader[node_] = self.leader
                    for child in newGraph[node_]:
                        if child not in self.visited:
                            stack2.append(child)
                scc_count[self.leader] = len(self.node_leader) - len_leader
        return scc_count

    def create_new_graph(self):
        newGraph = defaultdict(list)
        for node in self.graph:
            new_node = self.node_finish_time[node]
            for child in self.graph[node]:
                new_child = self.node_finish_time[child]
                newGraph[new_child].append(new_node)

        return newGraph


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(pow(10, 6))
    graph = defaultdict(list)
    graph[1] = [7]
    graph[2] = [5]
    graph[3] = [9]
    graph[4] = [1]
    graph[5] = [8]
    graph[6] = [3, 8]
    graph[7] = [9, 4]
    graph[8] = [2]
    graph[9] = [6]

    so = StronglyConnectedComponent(graph)
    out = so.find_scc()
    print(out)

    # so = StronglyConnectedComponent(get_qn_graph())
    # out = so.find_scc()
    # print(out)
    # print(sorted(list(out.values()))[:5])
