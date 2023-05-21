# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from base.linked_list.ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        pre, next_ = head, head.next
        while pre and next_:
            next_.next = pre
            pre.next = None
            next_ = pre.next
            pre = pre.next.next
