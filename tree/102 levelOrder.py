from base.tree.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        result, queue = [], [root]
        while queue:
            next_level, curr_vals = [], []
            for node in queue:
                if node.val is not None:
                    curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            result.append(curr_vals)
        return result


if __name__ == '__main__':
    tree = TreeNode.from_strs("[3, 9, 20, null, null, 15, 7]")
    print(tree)
    sol = Solution()
    t = sol.levelOrder(tree)
    print(t)
