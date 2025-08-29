# Depth First Search 🟢
# Given a Node class that has a name and an array of optional children nodes. When put together, nodes form a acyclic tree-like structure
# Implement the depthFirstSearch method on the Node class, which takes and empty array, traverses the tree using the depth-first search approach (navigating from left to right), stores all of the nodes' names in the input array and returns it

# Sample Input:
#         A
#       / | \
#      B  C  D
#     / \   / \
#    E   F G   H
#       / | \
#      I  J  K
# Sample Output: [A, B, E, F, I, J, C, D, G, K, H]
class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  # Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges (connections)
  # Space Complexity: O(V) where V is the number of vertices (nodes)
  def depthFirstSearch(self, array):
    array.append(self.name)
    for child in self.children:
      child.depthFirstSearch(array)
    return array

node1 = {
  "nodes": [
    {"children": ["B", "C", "D"], "id": "A", "value": "A"},
    {"children": ["E", "F"], "id": "B", "value": "B"},
    {"children": [], "id": "C", "value": "C"},
    {"children": ["G", "H"], "id": "D", "value": "D"},
    {"children": [], "id": "E", "value": "E"},
    {"children": ["I", "J"], "id": "F", "value": "F"},
    {"children": ["K"], "id": "G", "value": "G"},
    {"children": [], "id": "H", "value": "H"},
    {"children": [], "id": "I", "value": "I"},
    {"children": [], "id": "J", "value": "J"},
    {"children": [], "id": "K", "value": "K"}
  ],
  "startNode": "A"
}

node2 = {
  "nodes": [
    {"children": ["B", "C", "D", "E"], "id": "A", "value": "A"},
    {"children": [], "id": "B", "value": "B"},
    {"children": ["F"], "id": "C", "value": "C"},
    {"children": [], "id": "D", "value": "D"},
    {"children": [], "id": "E", "value": "E"},
    {"children": [], "id": "F", "value": "F"}
  ],
  "startNode": "A"
}

# Helper function to build the Node tree from the node dictionary
def build_tree(node_dict):
  nodes_map = {}
  # First, create all Node instances
  for n in node_dict["nodes"]:
    nodes_map[n["id"]] = Node(n["value"])
  # Then, add children
  for n in node_dict["nodes"]:
    parent = nodes_map[n["id"]]
    for child_id in n["children"]:
      parent.children.append(nodes_map[child_id])
  # Return the root node
  return nodes_map[node_dict["startNode"]]

# Build the tree and run depthFirstSearch
root1 = build_tree(node1)
result1 = root1.depthFirstSearch([])
print(result1)

root2 = build_tree(node2)
result2 = root2.depthFirstSearch([])
print(result2)