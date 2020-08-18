# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)


if __name__ == '__main__':
    listnode = ListNode(-10)
    listnode.next = ListNode(-3)
    listnode.next.next = ListNode(0)
    listnode.next.next.next = ListNode(5)
    listnode.next.next.next.next = ListNode(9)
    sol = Solution()
    res = sol.sortedListToBST(listnode)
    print(res)
