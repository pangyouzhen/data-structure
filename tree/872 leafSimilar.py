# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from base.tree.tree_node import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode):
            res, stack = [], [root]
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res

        left_val = dfs(root1)
        right_val = dfs(root2)
        if left_val == right_val:
            return True
        return False
