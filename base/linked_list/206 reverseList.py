# Definition for singly-linked list.
from typing import Optional
from base.linked_list.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp
        return

    def reverseList2(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = ListNode.from_list(nums)
    print(ln)
    sol = Solution()
    a = sol.reverseList(ln)
    print(a)
