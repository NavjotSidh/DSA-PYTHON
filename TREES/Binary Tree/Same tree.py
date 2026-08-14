class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Tree 1
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Tree 2
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

def same_tree(p,q):
    if p==None and q==None:
        return True
    if p==None or q==None:
        return False
    if p.val!=q.val:
        return False
    return same_tree(p.left,q.left) and same_tree(p.right,q.right)
print(same_tree(p,q))