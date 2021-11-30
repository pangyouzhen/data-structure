# Definition for singly-linked list.
from typing import Deque
from base.linked_list.ListNode import ListNode


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_int = int(self.reverseListNode(l1))
        l2_int = int(self.reverseListNode(l2))
        res = str(l1_int + l2_int)[::-1]
        dummy_head = ListNode(0)
        head = ListNode(0)
        dummy_head.next = head
        for i in res:
            head.next = ListNode(int(i))
            head =  head.next
        return dummy_head.next.next
        

    def reverseListNode(self, l: ListNode) -> str:
        res = []
        while l:
            res.append(str(l.val))
            l = l.next
        return "".join(res[::-1])


if __name__ == '__main__':
    l1 = ListNode.list2node([2, 4, 3])
    l2 = ListNode.list2node([5, 6, 4])
    sol = Solution()
    temp = (sol.addTwoNumbers(l1, l2))
    print(temp)
    # print(sol.reverseListNode(l1))
