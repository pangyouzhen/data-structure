from copy import deepcopy
from typing import List, Optional

from base.tree.tree_utils import print_btree
from collections import deque
import json


class TreeNode:
    node_id = 0

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # 内置的debug函数

    @classmethod
    def bst_from_list(cls, nums: List[int], bst_bool=True) -> Optional["TreeNode"]:
        """
        从列表生成树，中间节点作为root，sort_bool=True 默认生成二叉搜索树
        """

        # 设置闭包的原因是如果不用闭包，from_list每次都要传入bst_bool值
        def from_list_inner(nums: List[int]) -> Optional["TreeNode"]:
            """
            从列表生成树，sort_bool=True 默认生成二叉搜索树
            """
            if not nums:
                return
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = from_list_inner(nums[:mid])
            root.right = from_list_inner(nums[mid + 1:])
            return root

        if bst_bool:
            nums = [num for num in nums if num]
            nums.sort()
        return from_list_inner(nums)

    @classmethod
    def from_list(cls, data):
        # https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
        n = iter(data)
        tree = cls(next(n))
        fringe = deque([tree])
        while True:
            head = fringe.popleft()
            try:
                head.left = cls(next(n))
                fringe.append(head.left)
                head.right = cls(next(n))
                fringe.append(head.right)
            except StopIteration:
                break
        return tree

    def __str__(self):
        print_btree(self, lambda n: (str(n.val), n.left, n.right))
        return ""

    def __repr__(self):
        #  vs code debug工具
        graph = {
            "kind": {"graph": True},
            "nodes": [],
            "edges": []
        }

        def simple_order(root, last):
            if root:
                self.node_id += 1
                last_val = deepcopy(self.node_id)
                graph["nodes"].append(({'id': str(self.node_id), 'label': str(root.val)}))
                if last is not None:
                    graph["edges"].append(({
                        "from": str(last), "to": str(self.node_id)
                    }))
                simple_order(root.left, last=last_val)
                simple_order(root.right, last=last_val)

        simple_order(self, last=None)
        g = json.dumps(graph)
        return g


if __name__ == '__main__':
    nums = [1, 2, 2, None, 3, None, 3]
    sol = TreeNode.from_list(nums)
    print(sol)
    print("finish")
