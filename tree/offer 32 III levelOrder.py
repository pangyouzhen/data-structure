from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def left2right(i, next_level):
            if i and i.left:
                next_level.append(i.left)
            if i and i.right:
                next_level.append(i.right)

        if not root: return []
        res, queue = [], [root]
        while queue:
            next_level, curr_val = [], []
            for i in queue:
                if i and i.val is not None:
                    curr_val.append(i.val)
                    left2right(i, next_level)
            res.append(curr_val)
            queue = next_level
        result = []
        for i, v in enumerate(res):
            if i % 2 == 0:
                result.append(v)
            else:
                result.append(list(reversed(v)))
        return result


if __name__ == '__main__':
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(tree)
    sol = Solution()
    res = (sol.levelOrder(tree))
    print(res)
