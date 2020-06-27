from tree.bfs_dfs import TreeNode
from collections import deque


# dfs
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root):
            visited, stack = [], [root]
            while stack:
                fst = stack.pop()
                visited.append(fst.val)
                if fst.right:
                    stack.append(fst.right)
                if fst.left:
                    stack.append(fst.left)
            return visited


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)

    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    sol = Solution()
    print(sol.sumOfLeftLeaves(tree))
