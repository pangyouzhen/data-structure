from base.linked_list.ListNode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 增加虚拟头节点
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # 不断遍历判断
        # 需要重新赋值，不然就是在原元素上修改了
        prev = dummy_head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy_head.next


if __name__ == '__main__':
    ls = ListNode.list2node([1, 2, 6, 3, 4, 5, 6])
    func = Solution().removeElements
    print(func(ls, 6))
