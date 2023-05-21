# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from base.tree.tree_node import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        curr, res = [root], []
        while curr:
            curr_sum, next_level = 0, []
            for i in curr:
                if i and i.left:
                    next_level.append(i.left)
                if i and i.right:
                    next_level.append(i.right)
                if i:
                    curr_sum += i.val
            curr = next_level
            res.append(curr_sum)
        res.sort(reverse=True)
        if len(res) < k:
            return -1
        return res[k - 1]
