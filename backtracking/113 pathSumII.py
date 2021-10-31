from typing import List, Optional

from base.tree.tree_node import TreeNode


class Solution:
    # 这里的结果是List[List[int]] 所以每一步都应该有一个List[int] 作为one_ans
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        one_ans = [root.val]
        self.dfs(root, targetSum - root.val, one_ans)
        return self.res

    def dfs(self, root: Optional[TreeNode], targetSum: int, one_ans: List[int]):
        if targetSum == 0:
            # 注意这里是one_ans[:]
            self.res.append(one_ans[:])
            return
        # 因为是二叉树，所以只有左右两个节点
        for i in [root.left, root.right]:
            if i and i.val:
                # 注意回溯先回后溯，这里是先回
                one_ans.append(i.val)
                self.dfs(i, targetSum - i.val, one_ans)
                # 后溯
                one_ans.pop()


if __name__ == '__main__':
    tree = TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    print(tree)
    sol = Solution()
    print(sol.pathSum(tree, 22))
