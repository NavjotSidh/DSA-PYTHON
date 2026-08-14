class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Symmetric Tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

def mirror(left,right):
    if left==None and right==None:
        return True
    if left==None or right==None:
        return False
    if left.val!=right.val:
        return False
    return mirror(left.left,right.right) and mirror(left.right,right.left)

def is_symmetric(root):
    if root==None:
        return True
    return mirror(root.left,root.right)
print(is_symmetric(root))