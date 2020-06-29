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

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    linked_lst2 = LinkedList2(nums)
    print(linked_lst2)
