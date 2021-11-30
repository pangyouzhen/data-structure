# Definition for a binary tree node.
from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.a = []

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.rangeSumBST_me(root, L, R)
        return sum(self.a)

    def rangeSumBST_me(self, root, L, R):
        if root:
            if L <= root.val <= R:
                self.a.append(root.val)
            self.rangeSumBST_me(root.left, L, R)
            self.rangeSumBST_me(root.right, L, R)
