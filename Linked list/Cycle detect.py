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
g.next = c

head = a

slow=head
fast=head
ans="Cycle not detected"

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        ans="Cycle detected"
        break
print(ans)