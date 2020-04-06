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
            
r = Node(50)
insert(r,Node(20))
insert(r,Node(60))
insert(r,Node(40))
insert(r,Node(70))

def find_max(root):
    while root.right is not None:
        root = root.right
    return root.val

def find_min(root):
    while root.left is not None:
        root = root.left
    return root.val

print(find_min(r))
print(find_max(r))