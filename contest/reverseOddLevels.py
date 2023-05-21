from typing import Optional

from base.tree.tree_node import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res, curr = [TreeNode(root.val)], [root]
        level = 0
        while curr:
            curr_vals, next_level = [], []
            for i in curr:
                if i.left:
                    next_level.append(i.left)
                    curr_vals.append(TreeNode(i.left.val))
                if i.right:
                    next_level.append(i.right)
                    curr_vals.append(TreeNode(i.right.val))
            curr = next_level
            if level % 2 == 0:
                curr_vals = curr_vals[::-1]
            res.extend(curr_vals)
            level += 1
        kids = res[::-1]
        root = kids.pop()
        for node in res:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


if __name__ == '__main__':
    func = Solution().reverseOddLevels
    t = '[2,3,5,8,13,21,34]'
    tree = TreeNode.from_strs(t)
    print(tree)
    print(func(tree))
