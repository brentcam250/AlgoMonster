class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE


    def dfs(root, max):
      if max is None: 
        max = root.val
      if root is None:
        return 0

      if root.val > max:
          max = root.val
          return sum([dfs(root.left, max), dfs(root.right, max)]) # dont add one because this node isnt "visible"
    
      else: 
          return sum([dfs(root.left, max), dfs(root.right, max),1])

    return dfs(root, None)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)