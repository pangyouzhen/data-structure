# Definition for a binary tree node.
# 插入，删除，查找
from base.tree.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode):
        """
        :rtype:最高深度
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # max（left的深度+ right的深度） + 最后一个node
        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    root = "[3,9,20,null,null,15,7]"
    tree = TreeNode.from_strs(root)
    sol = Solution()
    assert sol.maxDepth(tree) == 3
