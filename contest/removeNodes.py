from typing import Optional
from base.linked_list.ListNode import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revers_head = self.reverse_listnode(head)
        fst = revers_head
        try:
            while revers_head:
                if revers_head.next.val < revers_head.val:
                    revers_head.next = revers_head.next.next
                revers_head = revers_head.next
        except AttributeError as e:
            print(e)
        return self.reverse_listnode(fst)

    def reverse_listnode(self, head):
        pre, curr = None, head
        while curr:
            # 多加了个指针
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp
        # curr 已经为None，所以返回pre
        return pre

if __name__ == "__main__":
    func = Solution().removeNodes
    node = ListNode.from_list([5,2,13,3,8])
    