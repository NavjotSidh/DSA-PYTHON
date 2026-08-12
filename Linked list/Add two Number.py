# List 1: 2 → 4 → 3
# List 2: 5 → 6 → 4
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def Add_two_num(l1,l2):
    dummy=Node(0)
    curr=dummy
    carry=0
    while l1 or l2 or carry:
        x=l1.val if l1 else 0
        y=l2.val if l2 else 0

        total=x+y+carry
        digit=total%10
        carry=total//10

        curr.next=Node(digit)
        curr=curr.next

        if l1:
            l1=l1.next
        if l2 :
            l2=l2.next
    return dummy.next