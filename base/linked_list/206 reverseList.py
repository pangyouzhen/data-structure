# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = ListNode.list2node(nums)
    sol = Solution()
    a = sol.reverseList(ln)
    print(a)
