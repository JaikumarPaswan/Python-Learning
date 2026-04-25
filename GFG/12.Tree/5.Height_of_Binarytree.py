#2 conventions for height: a) Number of Nodes on the longest root to leaf path
#b)Number of edges on the longest root to leaf path. In 2nd convention, the 
# root is not counted , so for an empty tree, length is -1. 
# We are following 1st convention

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


def height(root):
    if root==None:
        return 0
    else:
        lh=height(root.left)
        rh=height(root.right)
        return max(lh, rh)+1
    

#Shorter Implementation
# def height(root):
#     if root==None:
#         return 0
#     else:
#         return max(height(root.left), height(root.right))+1
    

print(height(root))
    
