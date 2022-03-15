from typing import List, Optional

from base.tree.tree_node import TreeNode


# TODO
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            if targetSum == root.val:
                # 这里返回的List[List[int]],这里靠猜的，后面debug下
                res.append([root.val])
        # 左子树到叶子节点的所有list
        left_ls: List[List[int]] = self.pathSum(root.left, targetSum - root.val)
        # [[4,11,2]]
        for i in left_ls:
            i.insert(0, root.val)
            res.append(i)
        right_ls = self.pathSum(root.right, targetSum - root.val)
        for j in right_ls:
            j.insert(0, root.val)
            res.append(j)
        return res


if __name__ == '__main__':
    tree = TreeNode.from_strs("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    print(tree)
    sol = Solution()
    print(sol.pathSum(tree, 22))
