from base.tree.tree_node import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res = []

        def dfs(root):
            queue = [root]
            while queue:
                element = queue.pop(0)
                res.append(element.val)
                if element.left:
                    dfs(root.left)
                if element.right:
                    dfs(root.right)

        dfs(root)
        return len(set(res)) == 1

if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode.from_list([2, 2, 2, 2, 5, ])
    print(tree)
    print(sol.isUnivalTree(tree))
