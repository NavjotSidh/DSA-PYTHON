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
ans=[]


def levelorder(root):
    queue=Queue()

    queue.push(root)
    ans.append([root.val])

    while queue.size()>0:
        l=queue.size()
        level = []
        for i in range(l):
            front=queue.pop()
            if front.left!=None:
                queue.push(front.left)
                level.append(front.left.val)
            if front.right!=None:
                queue.push(front.right)
                level.append(front.right.val)
        if len(level)>0:
            ans.append(level)
    return ans
levelorder(root)
print(ans)