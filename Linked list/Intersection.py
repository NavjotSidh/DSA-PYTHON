# List A: 1 → 2 → 3
#                  ↘
#                   7 → 8
#                  ↗
# List B:      4 → 5

def intersection(l1,l2):
    a=l1
    b=l2
    while a!=b:
        if a:
            a=a.next
        else:
            a=l2

        if b:
            b=b.next
        else:
            b=l1
    return a