# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head


if __name__ == '__main__':
    sol = Solution()
    head = ListNode.list2node([1, 2, 3, 3, 2, 1])
    head2 = ListNode.list2node([1, 2, 3])
    print(head)
    print(head2)
    print(sol.removeDuplicateNodes(head))
