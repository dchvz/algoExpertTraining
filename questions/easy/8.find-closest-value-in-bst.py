# Find Closest Value in BST 🟢
# Write a function that takes in a Binary Search Tree and a target integer and returns the closest value to the target.
# Each BST node has an integer value, a left child, and a right child.
# A Binary Search Tree (BST) is a tree data structure where each node follows the property:
# - The left subtree contains only nodes with values less than the node's value.
# - The right subtree contains only nodes with values greater than the node's value.

# Key takeaways, since it is BST! We know we can go to left or right depending on what we need
# Time Complexity O(logn) - on each step of the way we filter out half of the remaning tree
# Space Complexity O(1) - no auxiliar data structures are used

def find_closest_value_in_bst(tree, target):
  closest_value = float('inf')
  closest_diff = float('inf')
  while tree is not None:
      diff = abs(target - tree.value)
      if (diff < closest_diff):
          closest_diff = diff
          closest_value = tree.value
      if (tree.value < target):
          tree = tree.right
      elif (tree.value > target):
          tree = tree.left
      else:
          # both target and tree.value are equal
          break;

  return closest_value

# This is the class of the input tree. Do not edit.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def dict_to_bst(tree_data):
  node_map = {}
  # Create all BST nodes first
  for entry in tree_data["nodes"]:
    node_map[entry["id"]] = BST(entry["value"])
  # Link children
  for entry in tree_data["nodes"]:
    node = node_map[entry["id"]]
    left_id = entry.get("left")
    right_id = entry.get("right")
    if left_id:
      node.left = node_map[left_id]
    if right_id:
      node.right = node_map[right_id]
  return node_map[tree_data["root"]]


# Example usage:
tree = {
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": None, "right": None, "value": 22},
    {"id": "13", "left": None, "right": "14", "value": 13},
    {"id": "14", "left": None, "right": None, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": None, "right": None, "value": 5},
    {"id": "2", "left": "1", "right": None, "value": 2},
    {"id": "1", "left": None, "right": None, "value": 1}
  ],
  "root": "10"
}

tree2 = {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": None, "value": 55000},
      {"id": "1001", "left": None, "right": "4500", "value": 1001},
      {"id": "4500", "left": None, "right": None, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": None, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": None, "right": None, "value": 208},
      {"id": "206", "left": None, "right": None, "value": 206},
      {"id": "203", "left": None, "right": None, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": None, "right": "57", "value": 22},
      {"id": "57", "left": None, "right": "60", "value": 57},
      {"id": "60", "left": None, "right": None, "value": 60},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": None, "right": "1-3", "value": 1},
      {"id": "1-3", "left": None, "right": "1-4", "value": 1},
      {"id": "1-4", "left": None, "right": "1-5", "value": 1},
      {"id": "1-5", "left": None, "right": None, "value": 1},
      {"id": "-51", "left": "-403", "right": None, "value": -51},
      {"id": "-403", "left": None, "right": None, "value": -403}
    ],
    "root": "100"
  }


bst_root = dict_to_bst(tree)
result = find_closest_value_in_bst(bst_root, 12)
print(result)
bst_root2 = dict_to_bst(tree2)
result2 = find_closest_value_in_bst(bst_root2, 100)
print(result2)