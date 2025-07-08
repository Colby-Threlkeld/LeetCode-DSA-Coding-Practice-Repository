# creating tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# in order traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

print("In-Order:")
inorder(root)

# pre-order traversal
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

print("\n\nPre-Order:")
preorder(root)

# post-order traversal
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

print("\n\nPost-Order:")
postorder(root)

# BFS with dequeue
from collections import deque


def bfs(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("\n\nBFS:")
bfs(root)
