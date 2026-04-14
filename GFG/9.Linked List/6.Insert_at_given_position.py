# T.C:- θ(min(pos,n)) because is position is greater than the size, then at max loop will run n times
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertPos(head, pos, data):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    
    curr = head
    for i in range(pos-2):  #finding the node whose next node will be 'data'
        curr = curr.next
        if curr == None:
            return head
    
    temp.next = curr.next  #Do this step first otherwise, we will loose the rest of LinkedList
    curr.next = temp
    return head

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.key, end =" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

insertPos(head, 3, 25)

printLL(head)