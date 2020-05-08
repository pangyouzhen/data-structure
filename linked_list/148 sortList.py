# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pass

if __name__ == '__main__':
    sol = Solution()
    a = ListNode(4)
    a.next = ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)
    print(sol.sortList(a))
