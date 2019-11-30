# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


if __name__ == '__main__':
    ln = ListNode(1)
    ln.next = ListNode(1)
    ln.next.next = ListNode(2)

    ln2 = ListNode(1)
    ln2.next = ListNode(1)
    ln2.next.next = ListNode(2)
    ln2.next.next.next = ListNode(3)
    ln2.next.next.next = ListNode(3)
