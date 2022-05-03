from base.linked_list.ListNode import ListNode


class Solution:
    #  这里用了3个指针, 链表的首指针,当前指针和当前指针的前面一个指针
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if val == head.val:
            return head.next
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre,head = head,head.next
        while head:
            if head.val == val:
                pre.next = head.next
                return dummy_head.next
            else:
                pre = head
                head = head.next

if __name__ == "__main__":
    head = [4,5,1,9]
    val = 5
    lkl = ListNode.list2node(head)
    func = Solution().deleteNode
    print(func(lkl,val))