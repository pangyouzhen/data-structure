# Definition for a binary tree node.
from collections import deque
from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def is_even(l: List[int]):
            if l[0] % 2 != 0:
                return False
            for i in range(1, len(l)):
                if l[i] % 2 != 0:
                    return False
                if l[i] - l[i - 1] >= 0:
                    return False
            return True

        def is_odd(l: List[int]):
            if l[0] % 2 != 1:
                return False
            for i in range(1, len(l)):
                if l[i] % 2 != 1:
                    return False
                if l[i] - l[i - 1] <= 0:
                    return False
            return True

        res, queue = [], [root]
        a = 1
        while queue:
            next_level, curr_vals = [], []
            for i in queue:
                if i and i.val is not None:
                    curr_vals.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            queue = next_level
            if a % 2 == 1:
                if is_odd(curr_vals) is False:
                    return False
            else:
                if is_even(curr_vals) is False:
                    return False
            a += 1
        return True


if __name__ == '__main__':
    tree = TreeNode.from_list([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2])

    sol = Solution()
    t = sol.isEvenOddTree(tree)
    print(t)
