# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    print(sol.removeDuplicateNodes(head))
    assert sol.removeDuplicateNodes(head) == head2
