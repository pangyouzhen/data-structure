from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    # todo
    def findTilt(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 0
        left = self.findTilt(root.left)
        right = self.findTilt(root.right)
