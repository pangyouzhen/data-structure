# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head:
            res.append(str(head.val))
            head = head.next
        return int("".join(res), base=2)


if __name__ == '__main__':
    head = ListNode.list2node([1, 0, 1])
    sol = Solution()
    print(sol.getDecimalValue(head))
