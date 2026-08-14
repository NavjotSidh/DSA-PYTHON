class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right.left = TreeNode(12)
root.right.right = TreeNode(25)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(9)

def LCA(root,p,q):
    if p<root.val<q:
        return root.val
    elif p<root.val and q<root.val:
        
        return LCA(root.left,p,q)
    elif p>root.val and q>root.val:
        return LCA(root.right,p,q)
    return None
print(LCA(root,6,9))