# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(vals)
            current = next_level
        return res[::-1]


if __name__ == '__main__':
    tee = TreeNode(3)
    tee.left = TreeNode(9)
    tee.right = TreeNode(20)
    tee.right.left = TreeNode(15)
    tee.right.right = TreeNode(7)
    sol = Solution()
    print(sol.levelOrderBottom(tee))
