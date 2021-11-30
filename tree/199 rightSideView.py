# Definition for a binary tree node.
from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.right = TreeNode(5)
    tree.right = TreeNode(3)
    tree.right.right = TreeNode(4)
    print(tree)
    sol = Solution()
    print(sol.rightSideView(tree))
