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

def deletebst(root,target):
    if root is None:
        return None
    if target<root.val:
        root.left=deletebst(root.left,target)
    elif target>root.val:
        root.right=deletebst(root.right,target)
    else: #target==root
        if root.left==None and root.right==None:
            return None
        elif root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            root.val=temp.val
            root.right=deletebst(root.right,temp.val)
    return root
deletebst(root,12)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
inorder(root)