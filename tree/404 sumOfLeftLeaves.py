from tree.bfs_dfs import TreeNode
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        pass


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)

    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    sol = Solution()
    #  9+ 15  = 24
    print(sol.sumOfLeftLeaves(tree))
