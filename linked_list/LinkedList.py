# Linked list implementation in Python

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList2:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            # node = Node(data=nodes.pop(0))
            node = Node(nodes.pop(0))
            self.head = node
            for element in nodes:
                # node.next = Node(data=element)
                node.next = Node(element)
                node = node.next


if __name__ == '__main__':
    fst_node = Node("a")
    sed_node = Node("b")
    third_node = Node("c")
    fst_node.next = sed_node
    sed_node.next = third_node

    nodes = [fst_node, sed_node, third_node]
    linked_lst2 = LinkedList2(nodes)
