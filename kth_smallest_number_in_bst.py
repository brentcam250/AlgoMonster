class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(bst: Node, k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    val = None
    def tree_size(tree: Node, existing_k: int):
        nonlocal val 
        if val is not None: 
            return None
        if tree is None: 
            return 0
        left_size = tree_size(tree.left, existing_k)
        if val is not None: 
            return None 
        if left_size + existing_k == k - 1:
            val = tree.val 
            return None 
        right_size = tree_size(tree.right, existing_k + left_size + 1)
        if val is not None:
            return None
        return left_size + right_size + 1
    tree_size(bst,0)

    return   

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    k = int(input())
    res = kth_smallest(bst, k)
    print(res)