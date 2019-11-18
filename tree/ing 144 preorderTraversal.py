# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        vals = []
        while stack:
            node = stack.pop()
            if node:
                if node.val:
                    vals.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return vals

    def simplePreOrder(self, root: TreeNode):
        if root:
            print(root.val)
            self.simplePreOrder(root.left)
            self.simplePreOrder(root.right)

    def preorderRecursive(self, root: TreeNode) -> List[int]:
        return self.preorder(root, [])

    def preorder(self, node, vals):
        if node:
            if node.val:
                vals.append(node.val)
            vals = self.preorder(node.left, vals)
            vals = self.preorder(node.right, vals)
        return vals


if __name__ == '__main__':
    treeNode = TreeNode(25)
    treeNode.left = TreeNode(3)
    treeNode.right = TreeNode(4)
    treeNode.left.left = TreeNode(5)
    treeNode.left.right = TreeNode(6)

    sol = Solution()
    sol.simplePreOrder(treeNode)
    print(sol.preorderRecursive(treeNode))
    print(sol.preorderTraversal(treeNode))
