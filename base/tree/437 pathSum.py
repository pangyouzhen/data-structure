from base.tree.tree_node import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        注意：不从根节点开始，也不一定是叶子节点
        """
        if root is None:
            return 0
        res = self.root_path_sum(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    def root_path_sum(self, root: TreeNode, targetSum: int):
        # 包含root的值
        if root is None:
            return 0
        res = 0
        # 节点可能有负数
        if root.val == targetSum:
            res += 1
        res += self.root_path_sum(root.left, targetSum - root.val)
        res += self.root_path_sum(root.right, targetSum - root.val)
        return res


if __name__ == '__main__':
    tree = TreeNode.from_strs("[10,5,-3,3,2,null,11,3,-2,null,1]")
    func = Solution().pathSum
    targetSum = 8
    print(func(tree, targetSum))
