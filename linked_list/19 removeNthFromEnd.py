# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i

        index(head)
        return head.next


if __name__ == '__main__':
    ln = ListNode(1)
    ln.next = ListNode(2)
    ln.next.next = ListNode(3)
    ln.next.next.next = ListNode(4)
    ln.next.next.next.next = ListNode(5)
    sol = Solution()
    a = sol.removeNthFromEnd(ln, 2)
    print(a)
