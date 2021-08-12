# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.val = {}

    def __repr__(self):
        return str(self.val)


def createTrieFromPatterns(patterns):
    root = Node()
    for pattern in patterns:
        node = root
        for p in pattern:
            if p not in node.val:
                node.val[p] = Node()

            node = node.val[p]

    return root


def solve(text, n, patterns):
    result = []
    triePatterns = createTrieFromPatterns(patterns)
    i = 0
    while i < len(text):
        result += prefixTrieMatching(i, text, triePatterns)
        i += 1

    return result


def prefixTrieMatching(start, text, triePatterns):
    node = triePatterns
    begin = start
    while 1:
        if node.val == {}:
            return [begin]
        elif start < len(text) and text[start] in node.val:
            node = node.val[text[start]]
            start += 1

        else:
            # print("no matches found")
            return []


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
# text, n, patterns = "AAA", 1, ["AA"]
# text, n, patterns = "AA", 1, ["T"]
# text, n, patterns = "AATCGGGTTCAATCGGGGT", 2, ["ATCG", "GGGT"]
ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
