# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        pass


def dfs(root: TreeNode) -> List[int]:
    visited, stack = [root.val], [root]
    while stack:
        idx = stack.pop()
        if idx.left:
            stack.append(idx.left)
            visited.append(idx.left.val)
        if idx.right:
            stack.append(idx.right)
            visited.append(idx.right.val)
    return visited


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.right = TreeNode(5)
    sol = Solution()
    print(sol.binaryTreePaths(a))
    print(dfs(a))
