class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __repr__(self):
        return "Node({})".format(self.val)


class GetId:
    def __init__(self):
        self.id = 1

    def get(self):
        self.id += 1
        return self.id - 1


def create_power_law_tree(levels, k=3):
    from collections import deque
    q = deque()
    lev = 1
    idGetter = GetId()
    root = TreeNode(idGetter.get())
    q.append((root, lev))
    parent_map = {root: None}
    num_node_map = {}
    count = 1

    while lev <= levels:
        node_loop = []
        while q and q[0][1] == lev:
            node, l = q.popleft()
            node_loop.append(node)
            if l == levels:
                continue
            for _ in range(k):
                child = TreeNode(idGetter.get())
                count += 1
                node.children.append(child)
                parent_map[child] = node
                newLevel = l + 1
                q.append((child, newLevel))

        num_node_map[lev] = node_loop
        lev += 1
    print("Number of nodes = {}".format(len(num_node_map)))
    return root, parent_map, num_node_map


class BFS:
    def doBFS(self, parent_map, start_node, distance):

        from collections import deque
        q = deque([(start_node, 0)])
        visited_count = 0
        visited = {start_node}
        while q:
            node, dist = q.popleft()
            visited_count += 1
            if dist == distance:
                continue

            all_kinds = node.children + [parent_map[node]]

            for option in all_kinds:
                if option and option not in visited:
                    visited.add(option)
                    q.append((option, dist + 1))

        print('''All count except root = {}'''.format(visited_count - 1))


if __name__ == '__main__':
    root, parent_map, num_node_nap = create_power_law_tree(5, 3)
    so = BFS()
    queries = [(root, 3), (num_node_nap[5][0], 2)]
    for node, ttl in queries:
        print("Node = {}, ttl = {}".format(node, ttl))
        so.doBFS(parent_map, node, ttl)

    root3, parent_map4, num_node_nap4 = create_power_law_tree(4, 3)
    print(so.doBFS(parent_map4, num_node_nap4[2][0],3))
    print(so.doBFS(parent_map4, num_node_nap4[4][0],6))

