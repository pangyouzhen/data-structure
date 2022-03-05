from base.tree.tree_node import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        pass

if __name__ == '__main__':
    a = TreeNode.from_strs("[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]")
    sol = Solution()
    print(sol.convertBST(a))
