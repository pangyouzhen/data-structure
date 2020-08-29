# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        global a
        a = []
        self.rangeSumBST_me(root, L, R)
        return sum(a)

    def rangeSumBST_me(self, root, L, R):
        if root:
            if L <= root.val <= R:
                a.append(root.val)
            self.rangeSumBST_me(root.left, L, R)
            self.rangeSumBST_me(root.right, L, R)

