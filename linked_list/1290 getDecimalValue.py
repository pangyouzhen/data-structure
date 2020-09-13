# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head:
            res.append(str(head.val))
            head = head.next
        return int("".join(res), base=2)


if __name__ == '__main__':
    # head = [1, 0, 1]
    head = ListNode(0)
    # head.next = ListNode(0)
    # head.next.next = ListNode(1)
    sol = Solution()
    print(sol.getDecimalValue(head))
