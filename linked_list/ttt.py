class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == "__main__":
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    t = sol.reverseList2(a)
    print(t)
