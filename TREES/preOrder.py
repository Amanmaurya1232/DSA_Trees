class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def preorder(self,node):
        
        if node is None:
            return
        print(node.value,end="")
        self.preorder(node.left)
        self.preorder(node.right)
node=Node("A")
node.left=Node("B")
node.left.left=Node("C")
node.right=Node("D")
node.right.right=Node("E")
node.right.left=Node("F")
node.preorder(node)
