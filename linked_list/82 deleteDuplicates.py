from base.linked_list.ListNode import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        pass

if __name__ == '__main__':
    head1 = [1, 2, 3, 3, 4, 4, 5]
    head1 = ListNode.from_list(head1)
    head2 = [1, 1, 1, 2, 3]
    head2 = ListNode.from_list(head2)
    sol = Solution()
    print(sol.deleteDuplicates(head2))
    print(sol.deleteDuplicates(head1))
