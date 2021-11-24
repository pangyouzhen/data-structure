from base.tree.tree_node import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        level_values, queue = [], [root]
        while queue:
            next_level, curr_vals = [], []
            for i in queue:
                if i.val is not None:
                    curr_vals.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            queue = next_level
            level_values = curr_vals
        return level_values[0]


if __name__ == '__main__':
    tree = TreeNode.from_strs("[2, 1, 3]")
    sol = Solution()
    print(sol.findBottomLeftValue(tree))
