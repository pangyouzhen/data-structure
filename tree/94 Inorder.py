from typing import List

from base.tree.tree_node import TreeNode

# 前序，后续，中序 的不同指出和名称的意思 在于打印root value的位置不同
# Definition for a binary tree node.


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res


if __name__ == '__main__':
    sol = Solution()
    _ = "[10, 11, 5, null, null, 6, 3]"
    treenode = TreeNode.from_strs(_)
    print(treenode)
    print(sol.inorderTraversal(treenode))
