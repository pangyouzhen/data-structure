# Definition for a binary tree node.
from base.tree.tree_node import TreeNode

# 二叉查找树（英语：Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
#
# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于或等于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if not root: return
            inorder(root.left)
            if (self.prev is not None): self.min_diff = min(self.min_diff,root.val -self.prev)
            self.prev = root.val
            inorder(root.right)

        self.prev = None
        self.min_diff = float('inf')
        inorder(root)
        return self.min_diff

