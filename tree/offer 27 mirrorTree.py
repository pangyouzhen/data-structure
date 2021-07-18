from base.tree.tree_node import TreeNode
from typing import Optional


class Solution:
    def mirrorTree(self, root: TreeNode) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


if __name__ == '__main__':
    tree = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
    sol = Solution()
    a = sol.mirrorTree(tree)
    print(a)
