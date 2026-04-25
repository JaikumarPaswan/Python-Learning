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

import math

def getMax(root):
    if root==None:
        return -math.inf
    else:
        lm = getMax(root.left)
        rm = getMax(root.right)
        return max(root.key, lm, rm)


#shorter implementation
# def getMax(root):
#     if root==None:
#         return -math.inf
#     else:
#         return max(root.key, getMax(root.left), getMax(root.right))

print(getMax(root))


#T.C: θ(n)
#S.C: θ(h)
