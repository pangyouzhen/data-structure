# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1 = []
        # this is not suitable for (for key word),so use while
        h1 = l1
        while h1:
            ls1.append(str(h1.val))
            h1 = h1.next

        ls2 = []
        h2 = l2
        while h2:
            ls2.append(str(h2.val))
            h2 = h2.next

        res = int(''.join(ls1[::-1])) + int(''.join(ls2[::-1]))
        reversed_res = str(res)[::-1]
        head = temp = ListNode(reversed_res[0])
        for digit in reversed_res[1:]:
            temp.next = ListNode(int(digit))
            temp = temp.next
        return head

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))
