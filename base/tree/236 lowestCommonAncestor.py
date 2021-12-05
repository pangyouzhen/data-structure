from typing import Optional

from base.tree.tree_node import TreeNode


# todo
class Solution():
    # 注意这里和235题目的区别，这里不是二叉搜索树
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return
        if root.left is None and root.right is None:
            pass
        # 从root开始的值
        self.lowestCommonAncestor(root, p, q)
        # 不含有root的值
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)


if __name__ == "__main__":
    func = Solution().lowestCommonAncestor
    nums = "[3,5,1,6,2,0,8,null,null,7,4]"
    p = "[5,6,2,null,null,7,4]"
    p_tree = TreeNode.from_strs(p)
    q = "[1,0,8]"
    q_tree = TreeNode.from_strs(q)
    root = TreeNode.from_strs(nums)
    print(func(root, p_tree, q_tree))
