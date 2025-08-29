# Branch Sums 🟢
# Write a function that takes in a Binary tree and returns a list of its branch sums ordered from  leftmost branch sum to rightmost branch sum
# A branch sum is the sum of all values in a binary tree branch, which starts at the root node and ends at any leaf node

# Sample Input:
#         1
#        / \
#       2   3
#      / \
#     4   5
#    / \
#   6   7
# Sample Output: [13, 14, 8, 4]

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def branch_sums(root):
  results = []
  sumByTree = 0
  branch_sums_helper(root, sumByTree, results)
  return results

# Time Complexity O(n) where n is the number of nodes in the tree
# Space Complexity O(n) where n is the number of leaf nodes
def branch_sums_helper(root, sumByTree, results):
  if root is None:
    return 0
  sumByTree += root.value

  left = branch_sums_helper(root.left, sumByTree, results)
  right = branch_sums_helper(root.right, sumByTree, results)

  if left == 0 and right == 0:
    results.append(sumByTree)

  return sumByTree

tree1 = {
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": "10", "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9},
    {"id": "10", "left": None, "right": None, "value": 10}
  ],
  "root": "1"
}

tree2 = {
  "nodes": [
    {"id": "1", "left": None, "right": None, "value": 1}
  ],
  "root": "1"
}

def build_tree(tree_data):
    nodes = {}
    for node_info in tree_data["nodes"]:
        node = BinaryTree(node_info["value"])
        nodes[node_info["id"]] = node
    for node_info in tree_data["nodes"]:
        node = nodes[node_info["id"]]
        node.left = nodes.get(node_info["left"])
        node.right = nodes.get(node_info["right"])
    return nodes[tree_data["root"]]

root1 = build_tree(tree1)
print(branch_sums(root1))

root2 = build_tree(tree2)
print(branch_sums(root2))