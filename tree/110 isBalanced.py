from base.tree.tree_node import TreeNode


class Solution:

    def isBalanced(self, root: TreeNode):
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


if __name__ == '__main__':
    _ = [3, 9, 20, None, None, 15, 7]
    p1_tree = TreeNode.from_list(_)
    sol = Solution()
    assert sol.isBalanced(p1_tree) is True