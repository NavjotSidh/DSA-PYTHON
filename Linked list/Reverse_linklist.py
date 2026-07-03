class node:
    def __init__(self,val):
        self.val=val
        self.next=None
a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)
f=node(6)
g=node(7)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=None
head=a

curr=head
prev=None
nxt=None
while curr!=None:
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt
head=prev

cur=head

while cur!=None:
    print(cur.val)
    cur=cur.next
