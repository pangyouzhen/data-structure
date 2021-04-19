# Definition for a binary tree node.
from typing import List

from base.tree.tree_node import TreeNode


#  todo
#  错误的，想仿照排列数和组合数进行回溯，因为是树型结构，但是没成功
class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        res = []

        def dfs(root: TreeNode, total: int, one_ans):
            if sum(one_ans) == total:
                res.append(one_ans)
            if root.left:
                one_ans.append(root.val)
                dfs(root.left, total, one_ans)
                one_ans.pop()
            if root.right:
                one_ans.append(root.val)
                dfs(root.right, total, one_ans)
                one_ans.pop()

        one_ans = []
        dfs(root, total, one_ans)
        return res


if __name__ == '__main__':
    tree = TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    print(tree)
    sol = Solution()
    print(sol.pathSum(tree, 22))
