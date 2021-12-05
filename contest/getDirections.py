# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.left_all_ans = []
        self.right_all_ans = []

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pass

if __name__ == '__main__':
    root = "[5, 1, 2, 3, null, 6, 4]"
    tree = TreeNode.from_strs(root)
    sol = Solution()
    func = Solution().getsingleDiretions
    print(func(tree, 6, []))
    print(sol.left_all_ans)
