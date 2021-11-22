# Definition for a binary tree node.
from base.tree.tree_node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    root = '[4,2,7,1,3,6,9]'
    tree = TreeNode.from_strs(root)
    print(tree)
    sol = Solution().invertTree
    print(sol(tree))
