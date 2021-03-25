# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


if __name__ == '__main__':
    ln = ListNode.list2node([1, 1, 2])
    ln2 = ListNode.list2node([1, 1, 2, 3, 3])
    sol = Solution()
    print(sol.deleteDuplicates(ln))
    print(sol.deleteDuplicates(ln2))
