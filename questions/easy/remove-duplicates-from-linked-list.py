# Remove Duplicates from Linked List 🟢
# You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values
# Write a function that returns a modified version of the list that does not contain any nodes with duplicate values
# Sample Input: 1 -> 1 -> 2 -> 3 -> 3
# Sample Output: 1 -> 2 -> 3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Explanation: It's all in the pointers!
# If we want to remove duplicates, have to stay in the same position until the next node is not the same as the current one
# If the next node is equal to the current one, then we skip it
# If the next node is not equal to the current, then we validate the next different number on the list

# The reason we use current_node (cursor) instead of just node is so that we can return the whole list (with modifications)
# If we were to use just node, it would just return the last node after traversal

# Time Complexity: O(n), where n is the number of nodes in the linked list
# Space Complexity: O(1), because the list is being modified in place, the current_node variable is only a pointer/ref
def remove_duplicates_from_linked_list(node):
    current_node = node
    while current_node and current_node.next:
        if current_node.next.value == current_node.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return node;


def from_dict(data):
    nodes_map = {}
    # First, create all nodes
    for node_info in data["nodes"]:
        node_id = node_info["id"]
        nodes_map[node_id] = LinkedList(node_info["value"])
    # Then, link nodes
    for node_info in data["nodes"]:
        node_id = node_info["id"]
        next_id = node_info["next"]
        if next_id is not None:
            nodes_map[node_id].next = nodes_map[next_id]
    # Return the head node
    return nodes_map[data["head"]]

linked_list1 = from_dict({
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6}
    ]
})

linked_list2 = from_dict({
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "1-4", "value": 1},
        {"id": "1-4", "next": "1-5", "value": 1},
        {"id": "1-5", "next": "1-6", "value": 1},
        {"id": "1-6", "next": "1-7", "value": 1},
        {"id": "1-7", "next": None, "value": 1}
    ]
})

def print_linked_list(node):
    elements = []
    current = node
    while current:
        elements.append(str(current.value))
        current = current.next
    print(" -> ".join(elements))

print(print_linked_list(remove_duplicates_from_linked_list(linked_list1)))
print(print_linked_list(remove_duplicates_from_linked_list(linked_list2)))
