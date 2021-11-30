from typing import Optional

from base.tree.tree_node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)      
