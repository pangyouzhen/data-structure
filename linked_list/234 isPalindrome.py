from base.linked_list.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res == res[::-1]


if __name__ == '__main__':
    nums = [1, 2, 2, 1]
    ln = ListNode.list2node(nums)
    sol = Solution()
    print(sol.isPalindrome(ln))
