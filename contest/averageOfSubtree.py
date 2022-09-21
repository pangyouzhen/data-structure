from typing import List

from base.tree.tree_node import TreeNode

# TODO
class Solution:
    def averageOfSubtree(self, root : TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.averageOfSubtree(root.left)
        right = self.averageOfSubtree(root.right)
        return left + right

if __name__ =="__main__":
    func = Solution().averageOfSubtree
    nums ="[4,8,5,0,1,null,6]"
    root=TreeNode.from_strs(nums)
    print(func(root))