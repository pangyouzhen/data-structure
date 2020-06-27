class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left is None and right is None:
            return None
        if left is None:
            return right
        else:
            return left


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(6)

    sol = Solution()
    # print(sol.lowestCommonAncestor(tree, 5, 6))
