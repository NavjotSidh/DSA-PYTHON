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

def searchbst(root,target):
    if root.val==target:
        return True
    elif root.val<target:
        return searchbst(root.right,target)
    else:
        return searchbst(root.left,target)
# print(searchbst(root,6))

def validateBst(root,mn,mx):
    if root==None:
        return True
    if root.val<=mn or root.val>=mx:
        return False
    l=validateBst(root.left,mn,root.val)
    r=validateBst(root.right,root.val,mx)
    return r and l
# print(validateBst(root,float('-inf'),float('inf')))

def insertBST(root,key):
    newNode=TreeNode(key)
    if root==None:
        return newNode
    curr=root
    while curr!=None:
        if key<curr.val:
           if curr.left:
               curr=curr.left
           else:
               curr.left=newNode
               break
        else:
            if curr.right:
                curr=curr.right
            else:
                curr.right=newNode
                break
    return root
# insertBST(root,11)


def delete_bst(root,target):
    if root is None:
        return None
    if root.val>target:
        root.left= delete_bst(root.left,target)
    elif root.val<target:
        root.right= delete_bst(root.right,target)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            root.val=temp.val
            root.right= delete_bst(root.right,temp.val)
    return root
delete_bst(root,10)

ans=[]
def preorder(root):
    if root ==None:
        return ans
    ans.append(root.val)
    preorder(root.left)
    preorder(root.right)
preorder(root)
print(ans)