from base.tree.tree_node import TreeNode


class Solution:
    # 1. 最原始的做法：元素打印出来成为列表
    # 2. 
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def get_node_num(self, root: TreeNode):
        if root is None:
            return 0
        return self.get_node_num(root.left) + self.get_node_num(root.right) + 1

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        if root.left is None and k == 1:
            return root.val
        # 求左子树的节点数
        left_node_num = self.get_node_num(root.left)
        # 如果做子树的节点数加上1刚好等于k，说明root为所找的
        if k == left_node_num + 1:
            return root.val
        # 如果左子树的数量已经大于或等于k了，那么递归调用在做子树找第k个
        if k <= left_node_num:
            return self.kthSmallest2(root.left, k)
        # 如果左子树没法找到，那么就递归到右子树去找，数量要减去左子树和根
        if k > left_node_num:
            return self.kthSmallest2(root.right, k - left_node_num - 1)


if __name__ == '__main__':
    ls = '[3,1,4,null,2]'
    tree = TreeNode.from_strs(ls)
    print(tree)
    func = Solution().kthSmallest2
    print(func(tree, 4))
