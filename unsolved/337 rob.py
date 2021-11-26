from typing import Optional

from base.tree.tree_node import TreeNode


# TODO
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result, queue = [], [root]
        while queue:
            next_level, vals = [], []
            for node in queue:
                if node.val is not None:
                    vals.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            queue = next_level
            result.append(vals)
        odd = 0
        even = 0
        for i, v in enumerate(result):
            if i % 2 == 0:
                even += sum(v)
            else:
                odd += sum(v)
        return max(odd, even)


if __name__ == '__main__':
    sol = Solution()
    # tree = TreeNode.from_list([3, 2, 3, None, 3, None, 1])
    _ = "[4, 1, null, 2, null, 3]"
    tree = TreeNode.from_strs(_)
    print(tree)
    print(sol.rob(tree))
