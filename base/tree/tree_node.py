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
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
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
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    @classmethod
    def from_ls_int(cls, ls: List[Optional[int]]) -> 'Optional[TreeNode]':
        nodes = [cls(i) if i else None for i in ls]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

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

    def pre_order(self) -> List[int]:
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

    def level(root: "TreeNode") -> List[int]:
        """
        层次遍历
        :param root:
        :return:
        """
        if root is None:
            return []
        res, curr = [], [root]
        while curr:
            node = curr.pop(0)
            if node.left:
                curr.append(node.left)
            if node.right:
                curr.append(node.right)
            res.append(node.val)
        return res

    def levelOreder(root: "TreeNode") -> List[List[int]]:
        if root is None:
            return []
        res, curr = [], [root]
        while curr:
            next_vals, vals = [], []
            for node in curr:
                if node.left:
                    next_vals.append(node.left)
                if node.right:
                    next_vals.append(node.right)
                vals.append(node.val)
            curr = next_vals
            res.append(vals)
        return res


if __name__ == '__main__':
    nums = "[1, 2, 2, null, 3, null, 3]"
    sol = TreeNode.from_strs(nums)
    print(sol)
    print("finish")
