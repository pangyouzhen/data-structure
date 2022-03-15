# Definition for a binary tree node.

from base.tree.tree_node import TreeNode

# TODO
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


if __name__ == '__main__':
    func = Solution().recoverTree
    _ = "[1,3,null,null,2]"
    tree = TreeNode.from_strs(_)
    print(tree)
    func(tree)
    print(tree)
