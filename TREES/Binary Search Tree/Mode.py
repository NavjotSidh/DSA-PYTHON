class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Repeating values
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(3)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(7)

root.right.left.left = TreeNode(12)

def find(root):
    prev=None
    count=0
    mx_count=0
    Mode=[]
    def inorder(root):
        nonlocal prev, count, mx_count, Mode
        if root ==None:
            return
        inorder(root.left)
        if prev==root.val:
            count+=1
        else:
            count=1

        if count>mx_count:
            mx_count=count
            Mode=[root.val]
        elif count==mx_count:
            Mode.append(root.val)

        prev=root.val
        inorder(root.right)
    inorder(root)
    return Mode
print(find(root))
