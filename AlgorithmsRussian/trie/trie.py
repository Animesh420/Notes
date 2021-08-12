# Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    root = 0
    newNodeIndex = 0
    # write your code here
    for pattern in patterns:
        currentNode = root
        for p in pattern:
            if p in tree.get(currentNode, {}):
                currentNode = tree[currentNode][p]
            else:
                newNodeIndex = newNodeIndex + 1
                if currentNode not in tree:
                    tree[currentNode] = {}
                tree[currentNode].update({p: newNodeIndex})
                currentNode = newNodeIndex

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    # patterns = ["ATAGA", "ATC", "GAT"]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
