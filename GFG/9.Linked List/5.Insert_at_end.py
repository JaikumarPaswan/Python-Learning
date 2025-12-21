# T.C:- θ(n) for insert at end
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertEnd(head, key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.key, end =" ")
        curr = curr.next

 
head = None
head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)

printLL(head)

