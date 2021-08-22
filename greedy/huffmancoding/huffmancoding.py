"""
Huffman Coding 
Steps:
1. create a frequency min-heap
2. Extract two nodes with the minimum frequency from the min heap.
3. Create a new internal node with a frequency equal to the sum of the 
two nodes frequencies. Make the first extracted node as its left child 
and the other extracted node as its right child. Add this node to the min heap.

4. Repeat steps#2 and #3 until the heap contains only one node. The remaining
node is the root node and the tree is complete.
"""

class HuffNode:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol 
        self.freq = freq

        # symbol / character 
        self.symbol = symbol

        # left node of current node
        self.left = left

        # right node of current node
        self.right = right 

        # tree direction 
        self.huff = ''


def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)

    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} ---> {newVal}")


if __name__ == "__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freqs = [5, 9, 12, 13, 16, 45]

    nodes = []

    # converting into huffman tree nodes
    for i in range(len(freqs)):
        nodes.append(HuffNode(freqs[i], chars[i]))

    while len(nodes) > 1:

        # convert the tree into min-heap
        nodes = sorted(nodes, key= lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]

        left.huff = 0
        right.huff = 1

        newNode = HuffNode(left.freq+right.freq, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    printNodes(nodes[0])
