class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


    
def deleteNode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


printList(head)
deleteNode(head.next)
printList(head)