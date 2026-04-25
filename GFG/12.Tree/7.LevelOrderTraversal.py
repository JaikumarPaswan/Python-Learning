class Node:
    def __init__(self, k):
        self.left=None
        self.right=None
        self.key=k


root = Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

from collections import deque

def LOTraversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q)>0:
        node = q.popleft()
        print(node.key)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

LOTraversal(root)




#T.C: θ(n)
#S.C: O(n)