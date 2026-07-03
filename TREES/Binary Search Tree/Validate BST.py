from cmath import inf


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

def check(root,mn,mx):
    if root is None:
        return True
    if root.val<mn or root.val>mx:
        return False
    return check(root.left,mn,root.val-1) and \
    check(root.right,root.val+1,mx)
print(check(root,0,100))
