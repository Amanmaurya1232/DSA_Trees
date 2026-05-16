class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        
        self.postorder(node.right)
        print(node.value,end=",")
root=Node("A")
root.left=Node("B")
root.left.left=Node("C")
root.right=Node("D")
root.right.left=Node("E")
root.postorder(root)