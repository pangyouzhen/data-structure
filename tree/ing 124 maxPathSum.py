# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None:
            return 0
        leftMax = self.helper(root.left)
        rightMax = self.helper(root.right)
        # TODO ???
        # tempPath = root.val + leftMax + rightMax
        # sum = root.val + max(leftMax, rightMax, 0)
        # self.res = max(sum, tempPath, self.res)
        return sum


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
