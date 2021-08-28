# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

