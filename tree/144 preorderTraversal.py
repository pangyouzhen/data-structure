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
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
                res.append(temp.val)
        return res

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
    treenode = TreeNode(10)
    treenode.right = TreeNode(5)
    treenode.left = TreeNode(11)
    treenode.right.left = TreeNode(6)
    treenode.right.right = TreeNode(3)

    sol = Solution()
    # sol.simplePreOrder(treeNode)
    # print(sol.preorderRecursive(treeNode))
    print(sol.preorderTraversal(treenode))
