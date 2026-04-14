class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)



# def NthNodeEnd(H, n):
#     cur = H
#     if cur == None:
#         return 
    
#     count = 0
#     while cur:   #This statement is equal to 'while cur!=None'
#         cur=cur.next
#         count+=1

#     if count<n:
#         return

#     cur = H
#     for i in range(count-n):
#         cur = cur.next
#     return cur.key


# print(NthNodeEnd(head, 2))






#1)Move 'cur2' n positions ahead
#2)Start 'cur1' pointer from head
#3)Move both 'first' and 'second at same speed. When 'cur2'
# reaches Null, 'cur1' reaches required node

def NthNodeFromEnd(H, n):
    if H==None:
        return
    cur1 = H
    cur2 = H
    for i in range(n):
        if cur1 == None: #if n is greater than length of LL
            return
        cur2 = cur2.next
    
    while cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1.key

print(NthNodeFromEnd(head, 1))