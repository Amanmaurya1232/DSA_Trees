class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value,end=",")
        self.inorder(root.right)
node=Node("A")
node.left=Node("B")
node.left.left=Node("c")
node.right=Node("E")
node.right.right=N