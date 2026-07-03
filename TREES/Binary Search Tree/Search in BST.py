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

def Searchbst(root,target):
    curr = root
    while curr!=None:
        if curr.val==target:
            return curr
        elif curr.val>target:
            curr=curr.left
        elif curr.val<target:
            curr=curr.right
    return None
result=Searchbst(root,6)
if result:
    print("Found")
else:
    print("Not Found")

