from typing import List, Optional

from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self) -> None:
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return self.res
        one_ans = [root.val]
        self.path_sum(root, targetSum - root.val, one_ans)
        return self.res

    def path_sum(self, root: Optional[TreeNode], targetSum: int, one_ans: List[int]):
        if targetSum == 0 and root.left is None and root.right is None:
            self.res.append(one_ans[:])
        if targetSum != 0 and root.left is None and root.right is None:
            return
        for i in [root.left, root.right]:
            if i is not None:
                one_ans.append(i.val)
                self.path_sum(i, targetSum-i.val, one_ans)
                one_ans.pop()


if __name__ == '__main__':
    tree = TreeNode.from_strs("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    tree2 = TreeNode.from_strs("[-2,null,-3]")
    print(tree)
    # sol = Solution()
    print(Solution().pathSum(tree, 22))
    print(tree2)
    print(Solution().pathSum(tree2, -5))
