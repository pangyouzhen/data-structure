from tree.bfs_dfs import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = []
        if root is None:
            pass
        #      get 上一个元素
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)

    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    sol = Solution()
    print(sol.sumOfLeftLeaves(tree))
