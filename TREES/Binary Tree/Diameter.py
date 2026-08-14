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

def Diameter(root):
    diameter = 0

    def height_depth(root):
        nonlocal diameter

        if root == None:
            return 0

        left_height = height_depth(root.left)
        right_height = height_depth(root.right)

        diameter = max(diameter, left_height + right_height)

        return max(left_height, right_height) + 1

    height_depth(root)

    return diameter


print(Diameter(root))