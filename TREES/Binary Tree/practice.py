from collections import deque
def level_order(root):
    queue=deque()
    queue.append(root)
    ans=[[root.val]]
    while queue:
        l=len(queue)
        level=[]
        for i in range(l):
            front=queue.pop()
            if front.left!=None:
                queue.append(front.left)
                level.append(front.left)
            if front.right != None:
                queue.append(front.right)
                level.append(front.right)
        if len(level)>0:
            ans.append(level)
