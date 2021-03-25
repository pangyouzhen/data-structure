from typing import List
import json

class ListNode:
    # 只针对非循环链表
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list2node(cls, head: List[int]):
        # 这个式子是如何写出来的： 一般构造过程
        # ls5 = ListNode(5)
        # ls4 = ListNode(4, next=ls5)
        # ls3 = ListNode(3, next=ls4)
        # ls2 = ListNode(2, next=ls3)
        # ls1 = ListNode(1, next=ls2)
        head_ = head[::-1]
        curr = None
        ls = None
        for i in head_:
            ls = cls(val=i, next=curr)
            curr = ls
        return ls

    def __len__(self):
        res = 0
        a = self
        while a is not None:
            a = a.next
            res += 1
        return res

    def __str__(self):
        a = self
        res = ""
        while a is not None:
            res = res + str(a.val) + "->"
            a = a.next
        return res[:-2]

    def __repr__(self):
        graph = {
            "kind": {"graph": True},
            "nodes": [],
            "edges": []
        }
        a = self
        last_val = None
        while a is not None:
            graph["nodes"].append(({'id': str(a.val), 'label': str(a.val)}))
            # 链表必须要有两个节点
            if len(graph["nodes"]) > 1:
                graph["edges"].append(({
                    "from": str(last_val), "to": str(a.val)
                }))
            last_val = str(a.val)
            a = a.next
        graph = json.dumps(graph)
        return graph


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    listNode = ListNode.list2node(nums)
    print(len(listNode))
    print(listNode)
    print(listNode)
