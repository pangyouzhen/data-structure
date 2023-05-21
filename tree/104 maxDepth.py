# Definition for a binary tree node.
# 插入，删除，查找
from base.tree.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode):
        """
        :rtype:最高深度
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # max（left的深度+ right的深度） + 最后一个node
        return max(left_depth, right_depth) + 1

    def maxDepth2(self,root:TreeNode):
        if not root:
            return 0
        curr = [root]
        h = 0
        while curr:
            next_levels = []
            for i in curr:
                if i.left:
                    next_levels.append(i.left)
                if i.right:
                    next_levels.append(i.right)
            curr = next_levels
            h += 1
        return h
        
if __name__ == '__main__':
    root = "[3,9,20,null,null,15,7]"
    tree = TreeNode.from_strs(root)
    sol = Solution()
    sol2 = Solution().maxDepthTreave
    assert sol.maxDepth(tree) == 3
    print(sol2(tree))