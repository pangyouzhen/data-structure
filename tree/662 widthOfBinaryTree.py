from typing import Optional, List

from base.tree.tree_node import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res: int = 1
        curr: List[List[TreeNode, int]] = [[root, 1]]
        while curr:
            next_level, curr_val = [], []
            for i, index in curr:
                if i.left:
                    next_level.append([i.left, 2 * index])
                if i.right:
                    next_level.append([i.right, 2 * index + 1])
                curr_val = curr[-1][1] - curr[0][-1] + 1
            res = max(res, curr_val)
            curr = next_level
        return res


if __name__ == '__main__':
    root = TreeNode.from_strs('[1,3,2,5,null,null,9,6,null,7]')
    func = Solution().widthOfBinaryTree
    print(func(root))
