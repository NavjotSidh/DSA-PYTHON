from collections import deque
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

def insertbst(root,target):
    newNode=TreeNode(target)
    if root==None:
        return newNode
    curr=root
    while curr!=None:
        if target<curr.val:
            if curr.left!=None:
                curr=curr.left
            else:
                curr.left=newNode
                break
        else:
            if curr.right!=None:
                curr=curr.right
            else:
                curr.right=newNode
                break
insertbst(root,4)
ans=[]
def levelorder(root):
    queue=deque()

    queue.append(root)
    ans.append([root.val])

    while len(queue)>0:
        l=len(queue)
        level = []
        for i in range(l):
            front=queue.popleft()
            if front.left!=None:
                queue.append(front.left)
                level.append(front.left.val)
            if front.right!=None:
                queue.append(front.right)
                level.append(front.right.val)
        if len(level)>0:
            ans.append(level)
    return ans

print(levelorder(root))