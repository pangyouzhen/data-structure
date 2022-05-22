from base.linked_list.ListNode import ListNode


class Solution:
    #  这里用了2个指针, 首指针可以不用,当前指针和当前指针的前面一个指针
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if val == head.val:
            return head.next
        pre, curr = head, head.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
                return head
            else:
                pre = curr
                head = curr.next


if __name__ == "__main__":
    head = [4, 5, 1, 9]
    val = 5
    lkl = ListNode.from_list(head)
    func = Solution().deleteNode
    print(func(lkl, val))
