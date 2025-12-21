# Linked list does not stores values at contiguous location like list, each node has data and a reference to next node
# Final node will have reference 'None' which indicates that it is the last node

#Disadvantages 
# 1.No random access as lists
# 2.No cashe friendly


#Advantages
# 1. Insertion and deletion at begin and end is faster O(1), in list its O(n
# 2. Efficient for large data, No memory wastage


class Node:
  def __init__(self, k):
    self.key = k
    self.next = None
#Driver code
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
head = temp1


#Alternate shorter implementation
class Node:
  def __init__(self, k):
    self.key = k
    self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
