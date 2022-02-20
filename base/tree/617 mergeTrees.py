from typing import Optional

from base.tree.tree_node import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 只关注函数的宏观语义就好，不然容易陷入进去
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged


if __name__ == '__main__':
    root1 = TreeNode.from_strs("[1,3,2,5]")
    root2 = TreeNode.from_strs("[2,1,3,null,4,null,7]")
    print(root1)
    print(root2)
    sol = Solution()
    print(sol.mergeTrees(root1, root2))
