from base.tree.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(4)
    q.right = TreeNode(3)
    sol = Solution()
    assert sol.isSameTree(p, q) is False
