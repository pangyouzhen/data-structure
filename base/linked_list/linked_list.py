from typing import List


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.create_linked_List(nodes)

    def create_linked_List(self, nodes):
        if nodes is not None:
            # node = Node(data=nodes.pop(0))
            node = Node(nodes.pop(0))
            #  链表不同的是 一定要记住首要位置，指针不要跟着链表移动,最后返回头部就好
            #  链表两要素1. 固定指针 2. 移动指针
            self.head = node
            for element in nodes:
                # node.next = Node(data=element)
                node.next = Node(element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


if __name__ == '__main__':
    llist = LinkedList()
    fst_node = Node("a")
    llist.head = fst_node
    sed_node = Node("b")
    third_node = Node("c")
    fst_node.next = sed_node
    sed_node.next = third_node
    print(llist)

    t = ["a", "b", "c"]
    ls = LinkedList(t)
    print(ls)
