from base.tree.tree_node import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        pass

if __name__ == '__main__':
    a = TreeNode.from_list([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    sol = Solution()
    print(sol.convertBST(a))
