# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view


if __name__ == '__main__':
    tee = TreeNode(1)
    tee.left = TreeNode(2)
    tee.left.right = TreeNode(5)
    tee.right = TreeNode(3)
    tee.right.right = TreeNode(4)
    sol = Solution()
    print(sol.rightSideView(tee))
