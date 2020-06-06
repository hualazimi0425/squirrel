def getIntersectionNode(headA, headB):
    a, b = headA, headB
    while a != b:
        if a:
            a = a.next
        else:
            a = headB
        if b:
            b = b.next
        else:
            b = headA
    return a