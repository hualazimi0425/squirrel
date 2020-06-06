# solution 1 hash map
def detectCycle(head):
    nodeseen = set()
    while head != None:
        if head in nodeseen:
            return head
        else:
            nodeseen.add(head)
            head = head.next
    return None


# solution 2: Floyd's Tortoise and Hare
def getIntersect(self, head):
    tortoise, hare = head, head
    while hare is not None and hare.next is not None:
        hare = hare.next.next
        tortoise = tortoise.next
        if tortoise == hare:
            return tortoise
    return None


def detectCycle2(self, head):
    if head is None:
        return None
    intersect = self.getIntersect(head)
    if intersect is None:
        return None
    ptr1 = head
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1
