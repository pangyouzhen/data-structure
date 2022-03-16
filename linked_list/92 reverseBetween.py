from base.linked_list.ListNode import ListNode


class Solution:
    # TODO
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pass

    def reverse(self, head: ListNode):
        if head or head.next:
            return
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    func = Solution().reverseBetween
    print(func(head, left, right))
