from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(root, path, res):
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + root.val)
            return
        for child in root.children:
            if child is not None:
                path.append(root.val)
                dfs(child, path, res)
                path.pop()
    res = []
    if root: dfs(root, [], res)
    return res

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)