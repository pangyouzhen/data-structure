# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    a = [1, 2, 4]
    lna = ListNode.from_list(a)
    print(lna)
    b = [1, 3, 4]
    lnb = ListNode.from_list(b)
    print(lnb)
    sol = Solution()
    print(sol.mergeTwoLists(lna, lnb))
