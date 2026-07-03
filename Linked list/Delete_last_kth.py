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
n=3

curr=head
l=0
while curr!=None:
    curr=curr.next
    l+=1
p1=head
for i in range(l-n-1):
    p1=p1.next
p1.next=p1.next.next
cur=head
while cur!=None:
    print(cur.val)
    cur=cur.next
