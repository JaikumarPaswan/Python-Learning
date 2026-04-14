class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


    
def deleteNode(ptr): #It deletes a node without having access to the head. It works by copying next node’s data and skipping it
    temp = ptr.next
    ptr.key = temp.key
    ptr.next = temp.next



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


printList(head)
deleteNode(head.next)
printList(head)
