class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

#Mine Naive approach 2-traversals

# def countOfLL(H):  #function to calculate length of linkedlist
#     cur = H  #cur is a temporary variable used to store reference of a node
#     count = 0
#     if cur == None:
#         return count
#     else:
#         count = 1
#         while cur.next != None:
#             count += 1
#             cur = cur.next
#     return count


# def middle(H):  #function takes head of LL as argument
#     cur = H 
#     if countOfLL(H) == 0:
#         return 
#     elif countOfLL(H) == 1:
#         return cur.key
#     elif countOfLL(H) == 2:
#         return cur.next.key
#     else:
#         count = countOfLL(H)
#         p = 1
#         while p != (count//2)+1:
#             p+=1
#             cur=cur.next
#         return cur.key

# print(middle(head))


#GFG Naive approach 2-traversal, but 1 function only

# def printMiddle(H):
#     if H == None:
#         return
    
#     count = 0
#     cur = H
#     while cur:
#         cur = cur.next
#         count +=1

#     cur = H
#     for i in range(count//2):
#         cur = cur.next
#     print(cur.key)


    
def printMiddle(H):
    if head == None:
        return
    slow = head
    fast = head
    while fast != None and fast.next !=None:
        slow = slow.next
        fast = fast.next.next
    return slow.key

print(printMiddle(head))
