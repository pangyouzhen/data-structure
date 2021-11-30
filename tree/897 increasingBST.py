from base.tree.tree_node import TreeNode


class Solution:
    # todo
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []

        def Inorder(root):
            if root:
                Inorder(root.left)
                if root.val:
                    res.append(root.val)
                Inorder(root.right)

        Inorder(root)
        print(res)
        a = TreeNode(res[0])
        b = a
        for i in res[1:]:
            a.right = TreeNode(i)
            a = a.right
        return b


if __name__ == '__main__':
    # root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    root = [0, None, 1]
    root = TreeNode.from_list(root)
    print(root)
    func = Solution().increasingBST
    print(func(root))
