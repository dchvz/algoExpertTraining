# Middle Node 🟢
# you're given the head of a singly linked list, write a function that returns the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null if it's the tail of the list.
# Sample Input: 1 -> 2 -> 3 -> 4 -> 5
# Sample Output: 3 -> 5

class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

# Time Complexity O(n) where n is the elements in the linked list
# Space Complexity O(1)
def middle_node(linked_list):
  current_node = linked_list
  length = 0
  while current_node:
    current_node = current_node.next
    length +=1

  middle = int(length/2)+1
  for index in range(1, middle):
    linked_list = linked_list.next

  return linked_list

def create_linked_list(values):
  if not values:
    return None
  head = LinkedList(values[0])
  current = head
  for value in values[1:]:
    current.next = LinkedList(value)
    current = current.next
  return head

# Create three sample linked lists
list1 = create_linked_list([1, 2, 3, 4, 5])
list2 = create_linked_list([10, 20, 30, 40])
list3 = create_linked_list([7])

# Test middle_node function
print(middle_node(list1).value)  # Output: 3
print(middle_node(list2).value)  # Output: 30
print(middle_node(list3).value)  # Output: 7

