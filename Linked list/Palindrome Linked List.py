# Fast + Slow + Reverse
def is_palindrome(head):
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    prev=None
    while slow:
        nxt=slow.next
        slow.next=prev
        prev=slow
        slow=nxt
    left=head
    right=prev
    while right:
        if left.val != right.val:
            return False
        left=left.next
        right=right.next
    return True