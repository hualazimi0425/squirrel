class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
    def addAtHead(self, val):
        tmp = ListNode(val)
        if not self.head:
            self.head, self.tail = tmp, tmp
        else:
            tmp.next = self.head
            self.head = tmp
        self.size += 1
    def addAtTail(self,val):
        tmp = ListNode(val)
        if not self.head:
            self.head, self.tail = tmp, tmp
        else:
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1
    def addAtIndex(self, index, val):
        if index > self.size:
            return -1
        elif index == 0 or index == -1:
            self.addAtHead(val)
        else:
            tmp = ListNode(val)
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            tmp.next = cur.next
            cur.next = tmp
            if tmp.next is None:
                self.tail = tmp
            self.size += 1
    def deleteAtIndex(self, index):
        cur = self.head
        if index >= self.size or not self.head or index < 0:
            return -1
        elif index == 0:
            self.head = cur.next
            if not self.head:
                self.tail = None
        else:
            cur = self.head
            for _ in range(index - 1):
                if cur.next is None:
                    return
                cur = cur.next
            cur.next = cur.next.next
            if cur.next is None:
                self.tail = cur
        self.size = -1