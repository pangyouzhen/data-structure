from base.linked_list.ListNode import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> int:
        # 快慢指针的解法
        advance, last = head, head
        a = 0
        while a < k:
            advance = advance.next
            a += 1
        while advance:
            advance = advance.next
            last = last.next
        return last


if __name__ == '__main__':
    ls = ListNode.list2node([1, 2, 3, 4, 5])
    sol = Solution()
    print(sol.kthToLast(ls, 2))
