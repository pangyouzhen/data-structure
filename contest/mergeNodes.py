# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from base.linked_list.ListNode import ListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fst_head = ListNode(0)
        dummy_head = fst_head
        pre_val = 0
        vals = []
        while head:
            if head.val == 0:
                vals.append(pre_val)
                pre_val = 0
            else:
                pre_val += head.val
            head = head.next
        del vals[0]
        for i in vals:
            ls = ListNode(i)
            dummy_head.next = ls
            dummy_head = dummy_head.next
        return fst_head.next
