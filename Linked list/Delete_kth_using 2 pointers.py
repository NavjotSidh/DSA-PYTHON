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

p1=p2=head
# while p2 !=n+1:
for i in range(n):
    p2=p2.next
while p2.next!=None:
    p1=p1.next
    p2=p2.next
p1.next=p1.next.next
cur=head
while cur!=None:
    print(cur.val)
    cur=cur.next