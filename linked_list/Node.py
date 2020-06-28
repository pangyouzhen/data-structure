from typing import List


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


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

    # def __repr__(self):
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(node.data)
    #         node = node.next
    #     nodes.append("None")
    #     return "->".join(nodes)


# ERROR
# def create_listNode(nums: List[int]) -> LinkedList:
#     linkedList = LinkedList()
#     linkedList.head = ListNode(nums[0])
#     for i in nums[1:]:
#         linkedList.head.next = ListNode(i)
#         linkedList = linkedList.head.next
#     return linkedList


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5]
    # a = ListNode(0)
    # for i in nums:
    #     a.append(i)
    # print(a)
    # print("finished")
    # listNode = create_listNode(nums)
    # while listNode:
    #     print(listNode.val)
    #     listNode = listNode.next
    # print("finish")
    # a = ListNode(0)
    # a.next = ListNode(1)
    # a.next.next = ListNode(2)
    # print(a)
    llist = LinkedList()
    print(llist)
    fst_node = Node("a")
    llist.head = fst_node
    print(llist)
    sed_node = Node("b")
    third_node = Node("c")
    fst_node.next = sed_node
    sed_node.next = third_node
    print(llist)

    print("22222222222200")
    nodes = [fst_node, sed_node, third_node]
    linked_lst2 = LinkedList2(nodes)
    print(linked_lst2)
