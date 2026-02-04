# Linked list does not stores values at contiguous location like list, each node has data and a reference to next node
# Final node will have reference 'None' which indicates that it is the last node

#Disadvantages 
# 1.No random access as lists
# 2.No cashe friendly


#Advantages
# 1. Insertion and deletion at begin and end is faster O(1), in list its O(n)
# 2. Efficient for large data, No memory wastage


class Node:
  def __init__(self, k):  #This is the constructor of the class. It is called automatically when a new Node object is created. self refers to the current object. k is the value passed while creating the node.
    self.key = k          #This creates an instance variable named key. It stores the data/value of the node. The value of k is assigned to key.
    self.next = None      #This creates another instance variable called next. It will store the reference (address) of the next node in the linked list. None means this node is not pointing to any other node yet.
#Driver code
temp1 = Node(10) #Creates a new Node object with key = 10. temp1.next is automatically None.
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2 #Connects the first node (10) to the second node (20). Now temp1.next stores the address of temp2.
temp2.next = temp3
head = temp1


#So when you write:
#temp1 = Node(10)

#Python internally does:
#Node.__init__(temp1, 10)

#self.key = k     → temp1.key = 10
#self.next = None → temp1.next = None

#Each object of Node stores:
#  key → data
#  next → link to the next node

#This is the basic building block of a singly linked list.


#Alternate shorter implementation
class Node:
  def __init__(self, k):
    self.key = k
    self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
