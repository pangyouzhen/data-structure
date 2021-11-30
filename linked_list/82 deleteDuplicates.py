from base.linked_list.ListNode import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head

if __name__ == '__main__':
    head1 = [1, 2, 3, 3, 4, 4, 5]
    head1 = ListNode.list2node(head1)
    head2 = [1, 1, 1, 2, 3]
    head2 = ListNode.list2node(head2)
    sol = Solution()
    print(sol.deleteDuplicates(head2))
    print(sol.deleteDuplicates(head1))
