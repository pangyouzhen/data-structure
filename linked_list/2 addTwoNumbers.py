# Definition for singly-linked list.
from base.linked_list.ListNode import ListNode


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def linked_list_value(l1: ListNode) -> int:
            l1_value = []
            while l1 is not None:
                l1_value.append(str(l1.val))
                l1 = l1.next
            return int("".join(l1_value)[::-1])

        l1_value = linked_list_value(l1)
        # print(l1_value)
        l2_value = linked_list_value(l2)
        # print(l2_value)
        value_ = str(l1_value + l2_value)[::-1]

        dummy_head = ListNode(0)
        t = dummy_head
        for i in value_:
            curr = ListNode(val=int(i))
            t.next = curr
            t = t.next
        return dummy_head.next


if __name__ == '__main__':
    l1 = ListNode.list2node([2, 4, 3])
    l2 = ListNode.list2node([5, 6, 4])
    sol = Solution()
    temp = (sol.addTwoNumbers(l1, l2))
    print(temp)
