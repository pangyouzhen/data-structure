# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        #  这段代码的核心是 while curr: temp = curr.next, curr.next = pre,
        #  最后一行代码进行反转,再后面对curr和next pre进行移动
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    listNode.next.next.next = ListNode(4)
    listNode.next.next.next.next = ListNode(5)
    sol = Solution()
    a = sol.reverseList(listNode)
    # b = sol.reverseList2(listNode)
    print("finished")
