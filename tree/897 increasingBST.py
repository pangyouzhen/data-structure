from base.tree.tree_node import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []

        def Inorder(root):
            if root:
                Inorder(root.left)
                # 0 == False
                if root.val is not None:
                    res.append(root.val)
                Inorder(root.right)

        Inorder(root)
        # 无限循环下去的形式
        a = TreeNode(res[0])
        b = a
        for i in res[1:]:
            a.right = TreeNode(i)
            a = a.right
        return b


if __name__ == '__main__':
    # root = "[5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]"
    root = "[0,null,1]"
    root = TreeNode.from_strs(root)
    print(root)
    func = Solution().increasingBST
    print(func(root))
