class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.right.right = TreeNode(1)

def path_sum(root,targetsum):
    if root==None:
        return 0
    if root.left == None and root.right == None:
        return root.val == targetsum
    l=path_sum(root.left, targetsum - root.val)
    r=path_sum(root.right, targetsum - root.val)
    return l or r
print(path_sum(root,22))