class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.val < root.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

r = Node(40)
insert(r,Node(20))
insert(r,Node(65))
insert(r,Node(10))
insert(r,Node(60))
insert(r,Node(70))

def maximum(root):
    while root.right:
        root = root.right
    return root.val

def second_max(root):
    while root.right is not None:
        if root.right.left is None and root.right.right is None:
            return root.val
        elif root.right.right is None and root.right.left is not None:
            return maximum(root.right.left)

        root = root.right

print(second_max(r))