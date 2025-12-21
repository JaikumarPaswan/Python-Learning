# T.C:- O(1)
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def delFirst(head):
    if head == None:
        return None
    else:
        return head.next
    
def printLL(head):
    curr = head
    while curr!=None:
        print(curr.key, end =" ")
        curr = curr.next
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = delFirst(head)
printLL(head)