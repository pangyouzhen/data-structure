# Definition for a binary tree node.
from base.tree.tree_node import TreeNode

# todo
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 注意直接递归是不行的，因为可能出现right.left < root 的情况，所以需要另起一个函数记录当前的min和max
        return self.isBst(root, float("-inf"), float("inf"))

    def isBst(self, root: TreeNode, left_value: float, right_value: float):
        if root is None:
            return True
        if root.left is not None and root.right is not None:
            return root.left.val < root.val < root.right.val
        if root.left is None and root.right is not None:
            return root.val < root.right.val
        if root.left is not None and root.right is None:
            return root.left.val < root.val
        left_bool = self.isBst(root.left, root.val, float("inf"))
        right_bool = self.isBst(root.right, root.val, float("-inf"))
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
    assert func(tree1) is False
