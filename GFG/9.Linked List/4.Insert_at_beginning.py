# T.C:- θ(1) for insert at beginning
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertBegin(head, key):
    temp = Node(key)
    temp.next = head
    return temp
    

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.key, end =" ")
        curr = curr.next

#Driver code
head = None
head = insertBegin(head , 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)

print(printLL(head))

