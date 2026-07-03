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
k=8  #rotate by two digit

last=head
l=0
while last.next!=None:
    last=last.next
    l+=1
l+=1
k=k%l
curr=head
for i in range(l-k-1):
    curr=curr.next
last.next=head
head=curr.next
curr.next=None
cur=head
while cur!=None:
    print(cur.val)
    cur=cur.next