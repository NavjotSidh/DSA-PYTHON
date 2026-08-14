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

def balanced(root):

    def height(root):
        if root == None:
            return 0
        left_height=height(root.left)
        if left_height==-1:
            return -1

        right_height=height(root.right)
        if right_height== -1:
            return -1

        if abs(left_height-right_height)>1:
            return -1
        return max(left_height,right_height)+1
    return height(root)!= -1
print(balanced(root))