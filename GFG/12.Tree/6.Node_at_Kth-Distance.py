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

def printKDist(root, k):
    if root is None:
        return
    if k==0:
        print(root.key, end=" ")
    else:
        printKDist(root.left, k-1)
        printKDist(root.right, k-1)

printKDist(root, 2)