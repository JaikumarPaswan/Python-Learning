class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(30)


def removeDuplicate(H):
    if H==None:
        return
    
    cur = H
    while cur!=None and cur.next!=None:
        if cur.key == cur.next.key:
            cur.next = cur.next.next
        else:
            cur = cur.next


removeDuplicate(head)

def printLL(H):
    cur = H
    while cur:
        print(cur.key)
        cur = cur.next

printLL(head)