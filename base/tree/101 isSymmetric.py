# Definition for a binary treeTreeNode.
from tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRec(left.right, right.left) and self.isSymmetricRec(left.left, right.right)


if __name__ == '__main__':
    root = TreeNode.from_strs("[1, 2, 2, None, 3, None, 3]")
    print(root)
    sol = Solution()
    print(sol.isSymmetric(root))
