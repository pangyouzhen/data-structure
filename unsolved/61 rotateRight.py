from base.linked_list.ListNode import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        pass


if __name__ == '__main__':
    sol = Solution()
    head = [1, 2, 3, 4, 5]
    head = ListNode.list2node(head)
    k = 2
    print(sol.rotateRight(head, k))
