# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first, second = head, dummy
        for i in range(n):
            first = first.next
        while first:
            second, first = second.next, first.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    nums = [1, 2]
    ln = ListNode.from_list(nums)
    sol = Solution()
    a = sol.removeNthFromEnd(ln, 2)
    print(a)
