#Left Right Root

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

def preorder(root):
    if root!=None:
        preorder(root.left)
        preorder(root.right)
        print(root.key)

preorder(root)