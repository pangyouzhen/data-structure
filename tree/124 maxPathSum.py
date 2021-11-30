# Definition for a binary tree node.
from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            priceNewpath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, priceNewpath)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return int(self.maxSum)


if __name__ == '__main__':
    _ = [1, 2, 3]
    tree = TreeNode.from_list(_)
    _ = [-10, 9, 20, None, None, 15, 7]
    tree2 = TreeNode.from_list(_)
    sol = Solution()
    print(sol.maxPathSum(tree))
    print(sol.maxPathSum(tree2))
