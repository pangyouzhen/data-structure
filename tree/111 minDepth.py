# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1
        else:
            return min(left_depth, right_depth) + 1


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)

    tree3 = TreeNode(3)
    tree3.left = TreeNode(9)
    tree3.right = TreeNode(20)
    tree3.right.left = TreeNode(15)
    tree3.right.right = TreeNode(7)
    sol = Solution()
    # print(sol.minDepth(tree))
    # print(sol.minDepth(tree2))
    print(sol.minDepth(tree3))
