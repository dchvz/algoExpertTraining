# Node Depths 🟢
# The distance between a node in a Binary tree and the tree's root node is called the node's depth.
# Write a function that takes a Binary Tree and returns the sum of its nodes' depths.
# Each BinaryTree node has a `value` property, a `left` property pointing to the left child node, and a `right` property pointing to the right child node. The root node's depth is 0.

# Sample Input
# tree =
#         1
#        / \
#       2   3
#      / \
#     4   8
#    / \
#   5   6
# Sample Output: 12
## Explanation: The depths of the nodes are as follows:
# - Node 1 (root): depth 0
# - Node 2: depth 1
# - Node 3: depth 1
# - Node 4: depth 2
# - Node 8: depth 2
# - Node 5: depth 3
# - Node 6: depth 3

# Explanation:
# The function `node_depths` recursively calculates the sum of the depths of all nodes in a binary tree.
# It takes two parameters:
#   - `root`, which is the root node of the tree
#   - `depth`, which defaults to 0 and represents the current depth in the tree.
# If a node is None, it means it is child of a leaf node (bottom node)
# else, each level down means +1 in depth

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack.
def node_depths(root, depth = 0):
    if root is None:
        return 0
    return depth + node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Helper to build BinaryTree from dict
def build_tree(tree_dict):
    nodes = {node['id']: BinaryTree(node['value']) for node in tree_dict['nodes']}
    for node in tree_dict['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes.get(node['left'])
        if node['right']:
            nodes[node['id']].right = nodes.get(node['right'])
    return nodes[tree_dict['root']]

ex1 = {
    "tree": {
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9}
        ],
        "root": "1"
    }
}

ex2 = {
  "tree": {
    "nodes": [
      {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "1"
  }
}

ex3 = {
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": None, "value": 1},
      {"id": "2", "left": None, "right": None, "value": 2}
    ],
    "root": "1"
  }
}

tree1 = build_tree(ex1["tree"])
tree2 = build_tree(ex2["tree"])
tree3 = build_tree(ex3["tree"])
print(node_depths(tree1))
print(node_depths(tree2))
print(node_depths(tree3))