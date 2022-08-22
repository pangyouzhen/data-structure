from base.linked_list.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy_head1 = ListNode(0, head)
        dummy_head2 = ListNode(0, dummy_head1)
        fast, slow = head, dummy_head2
        while fast != slow:
            if fast and fast.next:
                fast, slow = fast.next.next, slow.next
            else:
                return False
        return True
