# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from base.linked_list.ListNode import ListNode
from copy import deepcopy
from math import floor


class Solution:
    # TODO
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        h = deepcopy(head)
        while head:
            head = head.next
            l += 1
        mid = floor(l / 2)
        t = 0
        if l == 1:
            return None
        if l == 2:
            return ListNode(h.val)
        dummy_head = ListNode(0)
        dummy_head.next = h
        while h:
            if t == mid:
                h.val = h.next.val
                h.next = h.next.next
            t += 1
            h = h.next
        return dummy_head.next


if __name__ == '__main__':
    # nums = [1, 3, 4, 7, 1, 2, 6]
    nums = [2, 1]
    # nums = [1, 2, 3, 4]
    ls = ListNode.list2node(nums)
    func = Solution().deleteMiddle
    print(ls)
    print(func(ls))
