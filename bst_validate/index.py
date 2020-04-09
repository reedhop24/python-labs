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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

inorder(r)

def isValidBST(self, root):
        if root is None:
            return True
        
        def dfs(node):
            queue = []
            queue.append(root)
            maximum = node.val
            minimum = node.val
            
            while len(queue) > 0:
                curr = queue.pop(0)
                if curr.val > maximum:
                    maximum = curr.val
                if curr.val < minimum:
                    minimum = curr.val
                    
                if curr.left is not None:
                    queue.append(curr.left)
                    if curr.left.val >= curr.val or curr.val > root.val and curr.left.val <= root.val or curr.left.val < minimum and curr.val != minimum:
                        return False
                if curr.right is not None:
                    queue.append(curr.right)
                    if curr.right.val <= curr.val or curr.val < root.val and curr.right.val >= root.val or curr.right.val > maximum and curr.val != maximum:
                        return False
        return False if dfs(root) == False else True