from typing import List
from base.linked_list.ListNode import ListNode


class Solution:
    def reversePrint(self, head: ListNode):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res[::-1]


if __name__ == '__main__':
    head = ListNode.from_list([1, 3, 2])
    sol = Solution()
    print(sol.reversePrint(head))
