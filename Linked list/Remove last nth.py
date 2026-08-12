class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = None
head=a
n=2

dummy=Node(0)
dummy.next=head
slow=dummy
fast=dummy

for i in range(n):
    fast=fast.next

while fast.next:
    fast=fast.next
    slow=slow.next
slow.next=slow.next.next

head=dummy.next
