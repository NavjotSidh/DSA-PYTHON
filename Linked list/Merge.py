class node():
    def __init__(self,val):
        self.val=val
        self.next=None
l1=node(1)
l1.next=node(3)
l1.next.next=node(5)

l2=node(2)
l2.next=node(4)
l2.next.next=node(6)

dummy=node(-1)
tail=dummy

while l1 and l2:
    if l1.val<=l2.val:
        tail.next=l1
        l1=l1.next
    else:
        tail.next=l2
        l2=l2.next
    tail=tail.next
if l1:
    tail.next=l1

if l2:
    tail.next=l2
curr=dummy.next
while curr!=None:
    print(curr.val)
    curr=curr.next