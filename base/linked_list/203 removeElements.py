from base.linked_list.ListNode import ListNode
from pysnooper import snoop


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 宏观语义：这个函数就是移除元素
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

    # @snoop()
    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        # 宏观语义：这个函数就是移除元素
        # 最基本的情况
        if head is None:
            return None
        res = self.removeElements2(head.next, val)
        # res 的含义表示移除相等的元素的情况
        # 此时head的情况,头部情况，这一点需要仔细考虑
        if head.val == val:
            return res
        else:
            head.next = res
            return head

    # 这种是错误的，思考下错误在哪里
    def removeElements3(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        res = self.removeElements(head.next, val)
        if res.val == val:
            return res.next
        else:
            return res


if __name__ == '__main__':
    ls = ListNode.list2node([1, 2, 6, 3, 4, 5, 6])
    # func = Solution().removeElements
    # print(func(ls, 6))
    func2 = Solution().removeElements2
    print(func2(ls, 6))
