from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def convert_list2listnode(cls, head: List[int]):
        head_ = head[::-1]
        curr = None
        listnode = None
        for i in head_:
            listnode = cls(val=i, next=curr)
            curr = listnode
        return listnode

    # TODO
    def __len__(self):
        res = 0
        _ = self
        while _:
            _ = _.next
            res += 1
        return res

    def __iter__(self):
        if self.next:
            return self.next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pass


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    al = ListNode.convert_list2listnode(a)
    print(len(al))
    print("finish")
    # list_node5 = ListNode(val=5)
    # list_node4 = ListNode(val=4, next=list_node5)
    # list_node3 = ListNode(val=3, next=list_node4)
    # list_node2 = ListNode(val=2, next=list_node3)
    # list_node = ListNode(val=1, next=list_node2)
    # # head = [1,2,3,4,5], left = 2, right = 4
    # # [1,4,3,2,5]
    # head = [1, 2, 3, 4, 5]
    # head_ = head[::-1]
    # curr = None
    # for i in head_:
    #     a = ListNode(val=i, next=curr)
    #     curr = a
    # print("finish")
