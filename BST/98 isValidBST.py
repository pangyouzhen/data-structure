# Definition for a binary tree node.
from base.tree.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 注意直接递归是不行的，因为可能出现right.left < root 的情况，所以需要另起一个函数记录当前的min和max
        return self.isBst(root, float("-inf"), float("inf"))

    def isBst(self, root: TreeNode, left_value: float, right_value: float) -> bool:
        if root is None:
            return True
        if root.val <= left_value or root.val >= right_value:
            return False
        # 对于左子树而讲，所有的节点应该都小于root节点
        left_bool = self.isBst(root.left, left_value, root.val)
        # 对于右子树而讲，所有的节点都应该大于root节点
        right_bool = self.isBst(root.right, root.val, right_value)
        return left_bool & right_bool


if __name__ == '__main__':
    func = Solution().isValidBST
    tree1 = "[2,1,3]"
    tree1 = TreeNode.from_strs(tree1)
    assert func(tree1) is True

    tree2 = "[5,1,4,null,null,3,6]"
    tree2 = TreeNode.from_strs(tree2)
    assert func(tree2) is False

    tree3 = "[5,4,6,null,null,3,7]"
    tree3 = TreeNode.from_strs(tree3)
    print(tree3)
    assert func(tree3) is False
