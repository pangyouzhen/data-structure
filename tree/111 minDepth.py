# Definition for a binary tree node.
from base.tree.tree_node import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        宏观语义：得到最小深度
        """
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1
        else:
            return min(left_depth, right_depth) + 1


if __name__ == '__main__':
    _ = [3, 9, 20, None, 4, 15, 7]
    tree = TreeNode.from_list(_)
    print(tree)
    sol = Solution()
    print(sol.minDepth(tree))
