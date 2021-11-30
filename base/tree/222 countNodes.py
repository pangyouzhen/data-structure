# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def countNodes(self, root: TreeNode) -> int:
        self.countNodes_(root)
        return self.res

    def countNodes_(self, root: TreeNode):
        if root:
            self.countNodes(root.left)
            self.countNodes(root.right)
            self.res += 1


if __name__ == '__main__':
    func = Solution().countNodes
    nums = "[]"
    tree = TreeNode.from_strs(nums)
    print(func(tree))
