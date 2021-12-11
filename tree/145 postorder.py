from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
                res.append(temp.val)
        return res[::-1]

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
    treenode = TreeNode(10)
    treenode.right = TreeNode(5)
    treenode.left = TreeNode(11)
    treenode.right.left = TreeNode(6)
    treenode.right.right = TreeNode(3)
    sol = Solution()
    print(sol.postOrderRecusive(treenode))
    # print(sol.postOrderRecusive(treenode))
    print(sol.postorderTraversal(treenode))