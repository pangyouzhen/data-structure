# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    def invertTreeFn(self, root: TreeNode):
        if root:
            invert = self.invertTreeFn
            root.left, root.right = invert(root.right), invert(root.left)
            return root

    def invertTreeTravserval(self, root: TreeNode):
        stack = [root]
        while stack:
            node = stack.pop()
            # pop 是作用在原始的数据结构上,赋值的是删除的值
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


if __name__ == '__main__':
    sol = Solution()
    treeNode = TreeNode(4)
    treeNode.left = TreeNode(2)
    treeNode.right = TreeNode(7)
    treeNode.left.left = TreeNode(1)
    treeNode.left.right = TreeNode(3)
    treeNode.right.left = TreeNode(6)
    treeNode.right.right = TreeNode(9)
    print(sol.invertTree(treeNode))
    print(sol.invertTreeTravserval(treeNode))
