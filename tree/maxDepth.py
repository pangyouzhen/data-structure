# Definition for a binary tree node.
# 插入，删除，查找
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    treeNode = TreeNode(3)
    treeNode.left = TreeNode(9)
    treeNode.right = TreeNode(20)
    treeNode.left.left = None
    treeNode.left.right = None
    treeNode.right.left = TreeNode(15)
    treeNode.right.right = TreeNode(7)

    sol = Solution()
    assert sol.maxDepth(treeNode) == 3