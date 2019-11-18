from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pass

    def simplePostOrder(self, root: TreeNode):
        if root:
            self.simplePostOrder(root.left)
            self.simplePostOrder(root.right)
            if root.val:
                print(root.val)

    def postOrderRecusive(self, root):
        return self.postOrder(root, [])

    def postOrder(self, root: TreeNode, vals):
        if root:
            vals = self.postOrder(root.left, vals)
            vals = self.postOrder(root.right, vals)
            if root.val:
                vals.append(root.val)
        return vals


if __name__ == '__main__':
    treenode = TreeNode(1)
    treenode.right = TreeNode(2)
    treenode.right.left = TreeNode(3)
    sol = Solution()
    sol.simplePostOrder(treenode)
    print(sol.postOrderRecusive(treenode))
