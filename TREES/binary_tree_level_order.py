from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def levelOrder(slef,root):
        result=[]
        if not root:
            return result
        queue=deque([root])
        while queue:
            size=len(queue)
            temp=[]
        
         


            for i in range(size):
                front_node=queue.popleft()
                temp.append(front_node.value)
                if front_node.left:
                    queue.append(front_node.left)
                if front_node.right:
                    queue.append(front_node.right)
            result.append(temp)
        return result
node=Node("A")
node.left=Node("B")
node.left.left=Node("C")
node.right=Node("E")
node.right.right=Node("d")
print(node.levelOrder(node))
