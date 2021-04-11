from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            next_level, curr_vals = [], []
            for i in queue:
                if i and (i.val is not None):
                    curr_vals.append(i.val)
                if i and i.left:
                    next_level.append(i.left)
                if i and i.right:
                    next_level.append(i.right)
            queue = next_level
            res.append(max(curr_vals))
        return res


if __name__ == '__main__':
    sol = Solution()
    pass
