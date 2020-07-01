# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_listnodes(nums: List[int]) -> ListNode:
    node = ListNode(nums.pop(0))
    #  链表不同的是 一定要记住首要位置，指针不要跟着链表移动,最后返回头部就好
    head = node
    for element in nums:
        # node.next = Node(data=element)
        node.next = ListNode(element)
        node = node.next
    return  head


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        reverse_headA = self.reverseListNode(headA)
        reverse_headB = self.reverseListNode(headB)
        while reverse_headA.val == reverse_headB.val:
            reverse_headA = reverse_headA.next
            reverse_headB = reverse_headB.next
        return self.reverseListNode(reverse_headA)

    def reverseListNode(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseListNode(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = create_listnodes(a)
    print('finish')
