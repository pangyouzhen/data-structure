from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 二叉树不是二叉搜索树
        if root:
            #  判断是叶子节点 + 左节点
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.res


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)

    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    sol = Solution()
    #  9+ 15  = 24
    print(sol.sumOfLeftLeaves(tree))
