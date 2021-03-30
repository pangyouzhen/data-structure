from typing import List, Optional

from base.tree.tree_utils import print_btree
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


if __name__ == '__main__':
    nums = [3, 2, 4, 6, 8, 5, 9]
    sol = TreeNode.from_list(nums)
    print(sol)
