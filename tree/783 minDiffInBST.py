from base.tree.tree_node import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []

        def inorder(root: TreeNode):
            if root:
                inorder(root.left)
                if root.val is not None:
                    res.append(root.val)
                inorder(root.right)

        inorder(root)
        min_val = float("inf")
        for i in range(1, len(res)):
            val = res[i] - res[i - 1]
            if val < min_val:
                min_val = val
        return min_val


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode.bst_from_list([4, 2, 6, 1, 3])
    a = sol.minDiffInBST(tree)
    print(a)
