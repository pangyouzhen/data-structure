# Definition for a binary tree node.
from typing import List

from base.tree.tree_node import TreeNode




class Solution:
    # def sumNumbers2(self, root: TreeNode) -> int:
    #     """
    #     从根节点到叶子节点的数字之和
    #     """
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:
    #         return root.val
    #     # 左子树
    #     left_sum: int = self.sumNumbers(root.left)
    #     # 5
    #     left_ = str(root.val)
    #     left_ += str(left_sum)
    #     # 右子树
    #     right_sum: int = self.sumNumbers(root.right)
    #     # 1
    #     right_ = str(root.val)
    #     right_ += str(right_sum)
    #     return int(left_) + int(right_)

    def sumNumbers(self, root: TreeNode) -> int:
        """
        从根节点到叶子节点的数字之和
        """
        res = self.sumNumbers_(root)
        res = [int(i) for i in res]
        return sum(res)

    def sumNumbers_(self, root: TreeNode) -> List[str]:
        """
        创建这个函数的原因是 # 输入：root = [4,9,0,5,1] 左边有两个路径495,491 那么左边应该返回是一个List [95,91],
        然后再去加上根节点， 用List[str]的原因是中间有00的情况，转化为int会丢掉
        :rtype: object
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        left_sum: List[str] = self.sumNumbers_(root.left)
        # [95,91]
        res = []
        for i in left_sum:
            res.append(str(root.val) + str(i))
        print(res)
        right_sum: List[str] = self.sumNumbers_(root.right)
        # [0]
        for j in right_sum:
            res.append(str(root.val) + str(j))
        return res


if __name__ == '__main__':
    # a = "[4,9,0,5,1]"
    # a = "[9,5,1]"
    a = "[5,3,2,7,0,6,null,null,null,0]"
    tree = TreeNode.from_strs(a)
    print(tree)
    func = Solution().sumNumbers
    print(func(tree))
