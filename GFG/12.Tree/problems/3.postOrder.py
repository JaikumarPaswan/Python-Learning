class Node:
    def __init__(self, k):
        self.left=None
        self.right=None
        self.data=k


root = Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)


class Solution:
    def preOrder(self, root):
        res=[]
        if root!=None:
            res += self.preOrder(root.left)
            res += self.preOrder(root.right)
            res.append(root.data)
        return res
    
sol = Solution()
print(sol.preOrder(root))

