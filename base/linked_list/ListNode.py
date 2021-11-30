import json
from typing import List, Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @classmethod
    # 以数组作为创建ListNode,java中的构造函数
    def list2node(cls, head: List[int]):
        # 创建非循环链表
        # 虚拟头节点
        assert len(head) > 0, "输入的是空的list，无法创建链表"
        fst_head = cls(val=0)
        dummy_head = fst_head
        for i in head:
            ls = cls(val=i)
            dummy_head.next = ls
            dummy_head = dummy_head.next
        return fst_head.next

    @classmethod
    # todo
    # 以数组作为创建ListNode,java中的构造函数
    def list2node_(cls, head: List[int]) -> 'ListNode':
        # 创建非循环链表
        # 虚拟头节点
        return cls.list2node__(head, 0)

    @classmethod
    def list2node__(cls, head: List[int], ind: int) -> "Optional[ListNode]":
        """
        :rtype: 返回创建的链表
        """
        if not head:
            return
        res = cls.list2node__(head[ind:], ind + 1)
        return res

    def __len__(self):
        if self.has_cycle():
            assert "这是一个环形链表，没有长度"
        res = 0
        a = self
        while a is not None:
            a = a.next
            res += 1
        return res

    def has_cycle(self):
        m = self
        a = set()
        # 一定注意这里的while m, while会判断 __bool__ __len__会进入到无限循环的情况
        while m is not None:
            if m in a:
                return True
            a.add(m)
            m = m.next
        return False

    def __str__(self):
        a = self
        res = ""
        while a is not None:
            res = res + str(a.val) + "->"
            a = a.next
        res += "end"
        return res

    def node2list(self):
        a = self
        res = []
        while a is not None:
            res.append(a.val)
            a = a.next
        return res == res[::-1]

    def __repr__(self):
        # vscode debug工具
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
    listNode = ListNode.list2node_(nums)
    # print(len(listNode))
    # print(listNode)
    print(listNode)
