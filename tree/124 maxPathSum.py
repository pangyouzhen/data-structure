# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
        return self.maxSum


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree2 = TreeNode(-10)
    tree2.left = TreeNode(9)
    tree2.right = TreeNode(20)
    tree2.right.left = TreeNode(15)
    tree2.right.right = TreeNode(7)
    sol = Solution()
    print(sol.maxPathSum(tree))
    print(sol.maxPathSum(tree2))
