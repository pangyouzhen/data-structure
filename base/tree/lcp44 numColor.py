from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def numColor(self, root: TreeNode) -> int:
        self.colors = []
        self.num_color(root) 
        return len(set(self.colors))

    def num_color(self,root:TreeNode):
        if root:
            if root.val:
                self.colors.append(root.val)
            if root.left:
                self.num_color(root.left)
            if root.right:
                self.num_color(root.right) 

if __name__ == "__main__":
    func = Solution().numColor
    root = TreeNode.from_strs("[1,3,2,1,null,2]")
    print(func(root))