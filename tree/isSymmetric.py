# Definition for a binary treeTreeNode.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    # root.right.right = TreeNode(3)
    sol = Solution()
    if sol.isSymmetric(root) == True:
        print("1")
    else:
        print("0")
