from base.tree.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    # todo
    def findTilt(self, root: TreeNode) -> int:
        pass
        # if root is None:
        #     return 0
        # left = self.findTilt(root.left)
        # right = self.findTilt(root.right)
        # if left is None and right is not None:
        #     self.res += abs(right.val)
        # elif right is None and left is not None:
        #     self.res += abs(left.val)
        # else:
        #     self.res += abs(left.val - right.val)
        # return self.res


class Solution2:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val


if __name__ == '__main__':
    func = Solution().findTilt
    _ = [4, 2, 9, 3, 5, None, 7]
    tree = TreeNode.from_list(_)
    print(func(tree))
