from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # out = []
        # 这里是投机取巧的方式，闭包里面使用了递归方法
        # def inorder(root):
        #     if not root:
        #         return
        #     else:
        #         inorder(root.left)
        #         out.append(root.val)
        #         inorder(root.right)
        #
        # inorder(root)
        #
        # return out
        stack, res = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def simpleInorder(self, root: TreeNode):
        if root:
            self.simpleInorder(root.left)
            print(root.val)
            self.simpleInorder(root.right)

    def inorderRecursive(self, root: TreeNode):
        return self.inorder(root, [])

    def inorder(self, root, vals):
        if root:
            vals = self.inorder(root.left, vals)
            if root.val:
                vals.append(root.val)
            vals = self.inorder(root.right, vals)
        return vals


if __name__ == '__main__':
    sol = Solution()
    treenode = TreeNode(1)
    treenode.right = TreeNode(2)
    treenode.right.left = TreeNode(3)
    print(sol.simpleInorder(treenode))
    print(sol.inorderRecursive(treenode))
    print(sol.inorderTraversal(treenode))
