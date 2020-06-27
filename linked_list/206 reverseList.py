# Definition for singly-linked list.
from ListNode import create_listNode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    listNode = create_listNode(nums)
    sol = Solution()
    print(sol.reverseList(listNode))
