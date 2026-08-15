class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(1)

root.left.left = TreeNode(9)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)

root.left.right.left = TreeNode(2)

root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(4)

def invert_tree(root):
    if root==None:
        return
    root.left,root.right=root.right,root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


ans=[]
def preorder(root):
    if root==None:
        return 0
    ans.append(root.val)
    preorder(root.left)
    preorder(root.right)
    return ans
# print(preorder(invert_tree(root)))
print(preorder(root))

