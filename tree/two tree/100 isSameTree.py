from base.tree.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        # both None
        if not p and not q:
            return True
        # any None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(4)
    q.right = TreeNode(3)
    sol = Solution()
    assert sol.isSameTree(p, q) is False
