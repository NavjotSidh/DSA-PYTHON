class node:
    def __init__(self,val):
        self.val=val
        self.next=None
a=node(1)
b=node(2)
c=node(2)
d=node(3)
e=node(3)
f=node(5)
g=node(6)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=None
head=a

curr=head
while curr!=None and curr.next!=None:
    if curr.next.val==curr.val:
        curr.next=curr.next.next
    else:
        curr = curr.next
cur=head
while cur!=None:
    print(cur.val)
    cur=cur.next