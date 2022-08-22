# Definition for a binary tree node.

from base.tree.tree_node import TreeNode


# TODO
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ans = []
        self.inorder(root)
        for i in self.ans:
            pass

    def inorder(self, root: TreeNode):
        if root:
            self.inorder(root.left)
            self.ans.append(root.val)
            self.inorder(root.right)


if __name__ == '__main__':
    func = Solution().recoverTree
    _ = "[3,1,null,null,2]"
    tree = TreeNode.from_strs(_)
    print(tree)
    # func(tree)
    # print(tree)
    print(Solution().inorder(tree))
