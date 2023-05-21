from base.linked_list.ListNode import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0, head)
        pre, next_ = dummy_head, head
        while True:
            if next_.val == val:
                pre.next = next_.next
                break
            else:
                pre, next_ = next_, next_.next
        return dummy_head.next


if __name__ == "__main__":
    func = Solution().deleteNode
    ls = ListNode.from_list([4, 5, 1, 9])
    print(func(ls, 1))
