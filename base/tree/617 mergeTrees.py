from typing import Optional

from base.tree.tree_node import TreeNode


class Solution:
    # TODO
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        合并好左子树
        """
        # if root1 is not None and root2 is not None:
        #     return TreeNode(root1.val + root2.val)
        # elif root1 is None and root2 is not None:
        #     return TreeNode(root2.val)
        # elif root1 is not None and root2 is None:
        #     return TreeNode(root1.val)
        # left_tree = self.mergeTrees(root1.left, root2.left)
        # right_tree = self.mergeTrees(root1.right, root2.right)


if __name__ == '__main__':
    root1 = TreeNode()
    root2 = TreeNode()
    sol = Solution()
    print(sol.mergeTrees(root1, root2))
