# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i

        index(head)
        # 链表递归的思想
        return head.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = ListNode.list2node(nums)
    sol = Solution()
    a = sol.removeNthFromEnd(ln, 2)
    print(a)
