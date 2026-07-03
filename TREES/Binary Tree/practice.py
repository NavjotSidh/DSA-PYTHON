class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1

    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q) == 0:
            return -1
        return self.q.pop(0)
    def getFront(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]
    def size(self):
        return len(self.q)-self.front
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(1)

root.left.left = TreeNode(9)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)

root.left.right.left = TreeNode(2)

root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(4)

ans=[]
def preorder(root):
    if root is None:
        return
    ans.append(root.val)
    preorder(root.left)
    preorder(root.right)
# preorder(root)
# print(ans)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    ans.append(root.val)
# postorder(root)
# print(ans)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    ans.append(root.val)
    inorder(root.right)
# inorder(root)
# print(ans)

def levelorder(root):
    if root is None:
        return
    queue=Queue()
    queue.push(root)
    ans.append([root.val])
    while queue.size() > 0:
        l = queue.size()
        level=[]
        for i in range(l):
            front=queue.pop()
            if front.left!=None:
                level.append(front.left.val)
                queue.push(front.left)
            if front.right!=None:
                level.append(front.right.val)
                queue.push(front.right)
        if len(level)>0:
            ans.append(level)
# levelorder(root)
# print(ans)

def height(root):
    if root is None:
        return 0
    maxleft=height(root.left)
    maxright=height(root.right)
    return max(maxleft,maxright)+1

