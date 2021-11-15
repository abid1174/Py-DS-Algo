"""
A program to execute depth first travarsal of a binary tree.
            A
          /   \
         B     C
        /  \     \
       D    E     F
    
Travarsal Values : A B D E C F

process: 
1. Insert A node to the stack and make the node as visited.
2. Check if the node has childs. If so, then push right child into the stack then left one. 

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth_first_travarsal(root):
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        print(current.data)

        if current.right: 
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node ("E")
    F = Node("F")

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    depth_first_travarsal(A)
