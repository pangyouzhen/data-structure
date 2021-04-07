# Definition for a binary tree node.
# 插入，删除，查找
from base.tree.tree_node import TreeNode


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    tree = TreeNode.from_list([3, 9, 20, 15, 7])
    sol = Solution()
    assert sol.maxDepth(tree) == 3
