# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res_ls = []
        while head:
            res_ls.append(head.val)
            head = head.next
        if len(res_ls) == 0:
            return
        res_ls.sort()
        node = ListNode(res_ls[0])
        new_head = node
        for i in res_ls[1:]:
            node.next = ListNode(i)
            node = node.next
        return new_head


if __name__ == '__main__':
    sol = Solution()
    a = ListNode(4)
    a.next = ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)
    b = sol.sortList(a)
    print(b)
