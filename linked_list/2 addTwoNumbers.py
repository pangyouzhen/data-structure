# Definition for singly-linked list.
from linked_list.ListNode import ListNode


class Solution:
    def __init__(self):
        self.linked_list = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1 = []
        self.str_sum(l1, ls1)
        ls2 = []
        self.str_sum(l2, ls2)
        print(ls1)
        print(ls2)

        ls1_number = int("".join(ls1))
        ls2_number = int("".join(ls2))

        sum_ = str(ls1_number + ls2_number)[::-1]
        node = ListNode(int(sum_[0]))
        self.linked_list = node
        print(sum_)
        for i in sum_[1:]:
            node.next = ListNode(int(i))
            node = node.next
        return self.linked_list

    def str_sum(self, node: ListNode, ls):
        if node:
            ls.append(str(node.val))
            self.str_sum(node.next, ls)


if __name__ == '__main__':
    l1 = ListNode.list2node([2, 4, 3])
    l2 = ListNode.list2node([5, 6, 4])
    sol = Solution()
    temp = (sol.addTwoNumbers(l1, l2))
    print(temp)
