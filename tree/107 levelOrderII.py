# Definition for a binary tree node.
from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res, current = [], [root]
        while current:
            next_level, curr_vals = [], []
            for node in current:
                if node.val is not None:
                    curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(curr_vals)
            current = next_level
        return res[::-1]


if __name__ == '__main__':
    tree = TreeNode.from_strs("[3, 9, 20, null, null, 15, 7]")
    print(tree)
    sol = Solution()
    print(sol.levelOrderBottom(tree))
