# Definition for singly-linked list.
from linked_list.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = ListNode.list2node(nums)
    sol = Solution()
    a = sol.reverseList(ln)
    print("finished")
