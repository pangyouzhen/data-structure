from base.linked_list.ListNode import ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res[len(res) - k]
#     TODO 链表快慢指针


