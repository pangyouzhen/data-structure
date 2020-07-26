# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import reduce


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []

        def inorder(root: TreeNode, res: List) -> List:
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
            return res

        result = inorder(root, res)
        mium_val = []
        for i in range(1, len(result)):
            mium_val.append(result[i] - result[i - 1])
        return min(mium_val)


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    a = sol.minDiffInBST(tree)
    print(a)
