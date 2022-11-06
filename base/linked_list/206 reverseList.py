# Definition for singly-linked list.
from typing import Optional
from base.linked_list.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp
        return

    def reverseList2(self, head: ListNode) -> ListNode:
        # 终止条件
        if head is None or head.next is None:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = ListNode.from_list(nums)
    print(ln)
    sol = Solution()
    a = sol.reverseList(ln)
    print(a)
