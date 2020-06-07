class ListNode:
    def __int__(self,val =0, next = None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(head):
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
