# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

if __name__ == '__main__':
    a = ListNode.list2node([1, 2, 3, 4, 5])
    print(a)
    sol = Solution()
    print(sol.swapPairs(a))
