# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    temp = (sol.addTwoNumbers(l1, l2))
    print(temp)
