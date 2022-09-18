"""
ID: alexlu.1
LANG: PYTHON3
TASK: heritage
"""

class Node:
    def __init__(self, letter):
        self.left = None
        self.right = None
        self.letter = letter

    def __str__(self):
        return f"{self.left.letter if self.left else None}, {self.right.letter if self.right else None}"

with open("heritage.in", "r") as f:
    inorder = f.readline().strip()
    preorder = f.readline().strip()

nodes = {i: Node(i) for i in inorder + preorder}

root = preorder[0]
for i in preorder[1:]:
    if inorder.index(i) < inorder.index(root):
        nodes[root].left = nodes[i]
    else:
        nodes[root].right = nodes[i]

    root = i

    if inorder.index(i) < len(inorder)-1:
        if preorder.index(inorder[inorder.index(i)+1]) < preorder.index(i):
            root = inorder[inorder.index(i)+1]

result = ""

def postorder(node):
    if node.left: postorder(node.left)
    if node.right: postorder(node.right)

    global result
    result += node.letter

root = nodes[preorder[0]]
postorder(root)

with open("heritage.out", "w") as f:
    f.write(f"{result}\n")