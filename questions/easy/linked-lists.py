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
def removeDuplicatesFromLinkedList(node):
    current_node = node
    while current_node and current_node.next:
        if current_node.next.value == current_node.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return node;



