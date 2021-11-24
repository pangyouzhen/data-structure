from base.tree.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        因为是一个二分搜索树
        """
        if root is None:
            return
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    root = "[6,2,8,0,4,7,9,null,null,3,5]"
    p = "[2,0,4,null,null,3,5]"
    q = "[4,3,5]"
    tree = TreeNode.from_strs(root)
    p_tree = TreeNode.from_strs(p)
    q_tree = TreeNode.from_strs(q)
    func = Solution().lowestCommonAncestor
    print(func(tree, p_tree, q_tree))
