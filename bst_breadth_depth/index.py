class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
insert(r,Node(20))
insert(r,Node(60))
insert(r,Node(30))
insert(r,Node(70))
insert(r,Node(10))
insert(r,Node(90))

print(inorder(r))

def bfs(root):
    if root is None:
        return -1

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].val)
        curr = queue.pop(0)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

def dfs(root):
    if root is None:
        return -1

    stack = []
    stack.append(root)

    while(len(stack) > 0):
        print(stack[len(stack)-1].val)
        curr = stack.pop(len(stack)-1)

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

print('bfs')
bfs(r)

print('dfs')
dfs(r)