from typing import List


class ListNode:
    """
    只针对非循环列表
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list2listnode(cls, head: List[int]):
        head_ = head[::-1]
        curr = None
        listnode = None
        for i in head_:
            listnode = cls(val=i, next=curr)
            curr = listnode
        return listnode

    def __len__(self):
        res = 0
        _ = self
        #  注意这里判断条件不能是 while _ 否则会陷入无限循环。因为while 会首先判断__bool__属性，随后判定__len__属性，进入无限循环
        while _ is not None:
            _ = _.next
            res += 1
        return res


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pass


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    al = ListNode.list2listnode(a)
    print(len(al))
    print("finish")
