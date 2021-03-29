from base.linked_list.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = set()
        while head:
            if head in a:
                return True
            a.add(head)
            head = head.next
        return False
