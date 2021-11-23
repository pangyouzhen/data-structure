from typing import List

from base.tree.tree_node import TreeNode


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
         返回所有从根节点到叶子节点的路径
        """
        #  思考下 这里res 换成 self.res 为什么不行
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res
        # 从根节点到左边叶子节点的路径，我只需要每一个都加下根节点就可以了，毕竟返回的从当前节点到叶子节点的路径了
        left_s: List[str] = self.binaryTreePaths(root.left)
        # ["2->5"]
        for i in range(len(left_s)):
            res.append(str(root.val) + "->" + left_s[i])

        right_s: List[str] = self.binaryTreePaths(root.right)
        # ['1->3']
        for j in range(len(right_s)):
            res.append(str(root.val) + "->" + right_s[j])

        return res


if __name__ == '__main__':
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(2)
    treeNode.left.right = TreeNode(5)
    treeNode.right = TreeNode(3)
    print(treeNode)
    sol = Solution()
    print(sol.binaryTreePaths(treeNode))
