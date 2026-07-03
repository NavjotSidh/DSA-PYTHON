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

# #Traversal of Linked List
# curr=head
# while curr!=None:
#     print(curr.val)
#     curr=curr.next

#Insert Node at End
# newNode=node(8)
# curr=head
# while curr.next!=None:
#     curr=curr.next
# curr.next=newNode
# curr1=head
# while curr1!=None:
#     print(curr1.val)
#     curr1=curr1.next

#Delete a Node
# k=3
# curr=head
# for i in range(k-1):
#     curr=curr.next
# curr.next=curr.next.next
# curr1=head
# while curr1!=None:
#     print(curr1.val)
#     curr1=curr1.next

#Middle Node (Brute force)
# curr=head
# l=0
# while curr.next!=None:
#     l+=1
#     curr=curr.next
# curr=head
# for i in range(l//2):
#     curr=curr.next
# print(curr.val)

#Middle Node (Slow/Fast Pointer)
# slow=head
# fast=head
# while fast.next and fast:
#     fast=fast.next.next
#     slow=slow.next
# print(slow.val)

#Detect Cycle (Floyd's Algorithm)
# fast=head
# slow=head
# while fast and fast.next:
#     fast=fast.next.next
#     slow=slow.next
#     if fast==slow:
#         cycle=True
#         break
# print(cycle)

#Reverse Linked List
# prev=None
# next=None
# curr=head
# while curr!=None:
#     next=curr.next
#     curr.next=prev
#     prev=curr
#     curr=next
# head=prev
# curr1=head
# while curr1!=None:
#     print(curr1.val)
#     curr1=curr1.next