# python3
import sys


class Node():
    def __init__(self):
        self.val = {}
        self.num = -1


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    fmt_text = text + "$"
    i = 0
    root = Node
    while i < len(text):
        root = insert_into_tree(start=i, root=root, text=fmt_text)
        i += 1

    return result


def insert_into_tree(start, root, text):
    node = root
    checkPoint = None
    while start < len(text):
        letter = text[start]
        if letter not in node.val:
            node.val[letter] = Node()
        else:
            checkPoint = start
        node = node.val[letter]
        start += 1
    

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
