class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def deleteLast(head):
    if head==None:
        return None
    
    if head.next == None:
        return None
    
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.key, end =" ")
        curr = curr.next
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = deleteLast(head)
printLL(head)