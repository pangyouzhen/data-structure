from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        visited, stack = [], [root]
        while stack:
            ver = stack.pop()
            if ver:
                pass


if __name__ == '__main__':
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(2)
    treeNode.left.right = TreeNode(5)
    treeNode.right = TreeNode(3)
    sol = Solution()
    print(sol.binaryTreePaths(treeNode))
