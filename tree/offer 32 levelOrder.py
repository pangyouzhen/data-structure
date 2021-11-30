from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res, queue = [], [root]
        while queue:
            curr = queue.pop(0)
            if curr and curr.val is not None:
                res.append(curr.val)
            if curr and curr.left:
                queue.append(curr.left)
            if curr and curr.right:
                queue.append(curr.right)
        return res


if __name__ == '__main__':
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(tree)
    sol = Solution()
    res = (sol.levelOrder(tree))
    print(res)
