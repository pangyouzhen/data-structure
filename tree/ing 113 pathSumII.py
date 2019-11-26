# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)
    sol = Solution()
    print(sol.pathSum(tree, 22))
