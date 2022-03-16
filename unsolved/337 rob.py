import opcode
from typing import Optional

from base.tree.tree_node import TreeNode


# TODO
class Solution:
    # bfs
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        pass
                    
            


if __name__ == '__main__':
    sol = Solution()
    # tree = TreeNode.from_list([3, 2, 3, None, 3, None, 1])
    _ = "[4, 1, null, 2, null, 3]"
    tree = TreeNode.from_strs(_)
    print(tree)
    print(sol.rob(tree))
