class Node:
  def __init__(self, key):
    self.key = key
    self.next = None



def search(head, x):
    i = 1
    curr = head
    while curr != None:
       if curr.key == x:
          return i
       else:
          curr = curr.next
          i+=1
    return -1


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


print(search(head,10))