from copy import deepcopy
from typing import List, Optional

from base.tree.tree_utils import print_btree
from collections import deque
import json


class TreeNode:
    #  二叉树
    node_id = 0

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # 内置的debug函数

    @classmethod
    # https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
    def from_strs(cls, string: str) -> 'Optional[TreeNode]':
        if string == '{}':
            return None
        nodes = [None if val.strip() == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # @classmethod
    # def bst_from_list(cls, nums: List[int], bst_bool=True) -> Optional["TreeNode"]:
    #     """
    #     从列表生成树，中间节点作为root，sort_bool=True 默认生成二叉搜索树
    #     """
    #
    #     # 设置闭包的原因是如果不用闭包，from_list每次都要传入bst_bool值
    #     def from_list_inner(nums: List[int]) -> Optional["TreeNode"]:
    #         """
    #         从列表生成树，sort_bool=True 默认生成二叉搜索树
    #         """
    #         if not nums:
    #             return
    #         mid = len(nums) // 2
    #         root = TreeNode(nums[mid])
    #
    #         root.left = from_list_inner(nums[:mid])
    #         root.right = from_list_inner(nums[mid + 1:])
    #         return root
    #
    #     if bst_bool:
    #         nums = [num for num in nums if num]
    #         nums.sort()
    #     return from_list_inner(nums)

    # @classmethod
    # def from_list(cls, data):
    #     # 对于root = [2,null,3,null,4,null,5,null,6] 生成是有问题的
    #     # https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    #     n = iter(data)
    #     tree = cls(next(n))
    #     fringe = deque([tree])
    #     while True:
    #         head = fringe.popleft()
    #         try:
    #             head.left = cls(next(n))
    #             fringe.append(head.left)
    #             head.right = cls(next(n))
    #             fringe.append(head.right)
    #         except StopIteration:
    #             break
    #     return tree

    def __str__(self):
        print_btree(self, lambda n: (str(n.val), n.left, n.right))
        return ""

    # def __repr__(self):
    #     #  vs code debug工具
    #     graph = {
    #         "kind": {"graph": True},
    #         "nodes": [],
    #         "edges": []
    #     }
    #
    #     def simple_order(root, last):
    #         if root:
    #             self.node_id += 1
    #             last_val = deepcopy(self.node_id)
    #             graph["nodes"].append(({'id': str(self.node_id), 'label': str(root.val)}))
    #             if last is not None:
    #                 graph["edges"].append(({
    #                     "from": str(last), "to": str(self.node_id)
    #                 }))
    #             simple_order(root.left, last=last_val)
    #             simple_order(root.right, last=last_val)
    #
    #     simple_order(self, last=None)
    #     g = json.dumps(graph)
    #     return g

    def pre_order(self):
        res = []

        def pre_order_closure(root):
            if root:
                res.append(root.val)
                pre_order_closure(root.left)
                pre_order_closure(root.right)

        pre_order_closure(self)
        return res

    def in_order(self):
        res = []

        def in_order_closure(root):
            if root:
                in_order_closure(root.left)
                res.append(root.val)
                in_order_closure(root.right)

        in_order_closure(self)
        return res

    def post_order(self):
        res = []

        def post_order_closure(root):
            if root:
                post_order_closure(root.left)
                post_order_closure(root.right)
                res.append(root.val)

        post_order_closure(self)
        return res

    def __len__(self):
        # 树的深度
        return self.depth()

    def depth(self):
        def maxDepth(root):
            #  is None
            if root is None:
                return 0
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            return max(left_depth, right_depth) + 1

        return maxDepth(self)


if __name__ == '__main__':
    nums = [1, 2, 2, None, 3, None, 3]
    sol = TreeNode.from_list(nums)
    print(sol)
    print("finish")
