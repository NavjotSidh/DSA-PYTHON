from operator import truediv


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

def searchsbt(root,target):
    curr=root
    while curr!=None:
        if target==curr.val:
            return curr
        elif target<curr.val:
            curr=curr.left
        else:
            curr=curr.right

def insertbst(root,key):
    newNode=TreeNode(key)
    if root is None:
        return newNode
    curr=root
    while curr!=None:
        if key<curr.val:
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

def deletebst(root,target):
    if root is None:
        return None
    if target<root.val:
        root.left=deletebst(root.left,target)
    elif target>root.val:
        root.right=deletebst(root.right,target)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            temp=root.right
            while temp!=None:
                temp=temp.left
            root.val=temp.val
            root.right=deletebst(root.right,temp.val)
    return root

def validatebst(root,mn,mx):
    if root is None:
        return True
    if root.val<mn or root.val>mx:
        return False
    checkLeft=validatebst(root.left,mn,root.val-1)
    checkRight=validatebst(root.right,root.val+1,mx)
    return checkLeft and checkRight
print(validatebst(root,0,100 ))