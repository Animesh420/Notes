import networkx as nx
def read_graph():
    filepath = r"C:\Users\anime\PycharmProjects\PyDSA\Coursera\courseraStanford\GraphShortestPath\week2\dijkstra_data.txt"
    graph = {}
    G = nx.Graph()
    with open(filepath, "r") as f:

        for line in f:
            info = line.split("\t")

            vertex = int(info[0])
            graph[vertex] = []
            for element in info[1:-1]:
                child, weight = element.split(",")
                child, weight = int(child), int(weight)
                graph[vertex].append((child, weight))
                G.add_edge(vertex, child, weight=weight)

    return graph, G


class Dijkstra:

    def shortestPath(self, source, graph, nodes, print_=False):

        seen = {source: 0}

        while len(seen) < len(nodes):
            global_min_dist = float("inf")
            end = None
            for node, distance in seen.items():

                for child, weight in graph[node]:

                    if child not in seen:

                        new_distance = distance + weight
                        if new_distance < global_min_dist:
                            global_min_dist = new_distance
                            end = child
            seen[end] = global_min_dist

        if print_:
            for x in nodes:
                print("Shortest distance of node {} from source node {} is {}".format(x, source, seen[x]))

        return seen

    def dijkstraFaster(self, source, graph, nodes):
        pass


if __name__ == '__main__':
    so = Dijkstra()
    from collections import defaultdict

    graph = defaultdict(list)
    graph["s"] = [("v", 1), ("w", 4)]
    graph["v"] = [("t", 6), ("w", 2)]
    graph["w"] = [("t", 3)]
    # so.shortestPath(source="s", graph=graph, nodes=["s", "w", "v", "t"], print_=True)
    g, nx_g = read_graph()
    seen = so.shortestPath(source=1, graph=g, nodes=list(range(1, 201)))
    qn = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    ans = [str(seen[x]) for x in qn]
    print(",".join(ans))
