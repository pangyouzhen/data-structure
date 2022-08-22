# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        reverse_headA = self.reverseListNode(headA)
        reverse_headB = self.reverseListNode(headB)
        while reverse_headA.val == reverse_headB.val:
            reverse_headA = reverse_headA.next
            reverse_headB = reverse_headB.next
        return self.reverseListNode(reverse_headA)

    def reverseListNode(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseListNode(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    ln = ListNode.from_list(a)

