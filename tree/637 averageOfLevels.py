# Definition for a binary tree node.
from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res, queue = [], [root]
        while queue:
            next_level, curr_vals = [], []
            for q in queue:
                if q is not None and (q.val is not None):
                    curr_vals.append(q.val)
                if q.left:
                    next_level.append(q.left)
                if q.right:
                    next_level.append(q.right)
            queue = next_level
            curr_avg = sum(curr_vals) / (len(curr_vals))
            res.append(curr_avg)
        return res


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(sol.averageOfLevels(tree))
