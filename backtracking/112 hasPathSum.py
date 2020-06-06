class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)
    sol = Solution()
    print(sol.hasPathSum(tree, 22))
