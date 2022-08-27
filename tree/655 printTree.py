from typing import List, Optional
from base.tree.tree_node import TreeNode


class Solution:
    def printTree(self, root: TreeNode) -> List[List[int]]:
        def depth(root: TreeNode):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1

        height = depth(root)
        m = height
        n = 2 ** m - 1
        ans = [[''] * n for _ in range(m)]

        def dfs(node: TreeNode, r: int, c: int):
            # print(r, c)
            ans[r][c] = str(node.val)
            if node.left:
                dfs(node.left, r + 1, c - 2 ** (height - 1 - r - 1))
            if node.right:
                dfs(node.right, r + 1, c + 2 ** (height - 1 - r - 1))

        dfs(root, 0, (n - 1) // 2)
        return ans


if __name__ == '__main__':
    tree = TreeNode.from_strs('[1,2,3,null,4,5,6]')
    func1 = Solution().printTree
    print(func1(tree))
