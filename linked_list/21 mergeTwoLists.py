# Definition for singly-linked list.
#  对于链表的问题，一定想到递归， h1 = h1.next 配合递归

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        res.append(str(self.val))
        while self.next:
            res.append(str(self.next.val))
            self.next = self.next.next
        return ",".join(res)


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
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(4)
    print(a)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    print(b)
    sol = Solution()
    print(sol.mergeTwoLists(a, b))
