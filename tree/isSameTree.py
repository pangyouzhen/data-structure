# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        # 一个成熟的coder必须考虑到各种异常的情况.和如何进行扩展
        # self.isSame(p, q)
        # left_bool, right_bool = True, True
        # output_bool = False
        # while (left_bool and right_bool):
        #     if p.left is not None and q.left is not None:
        #         p, q = p.left, q.left
        #         left_bool = self.isSame(p, q)
        #     else:
        #         return False
        #     if q.right is not None and q.right is not None:
        #         p_right, q_right = p.right, q.right
        #         right_bool = self.isSame(p_right, q_right)
        # return output_bool
        pass

    def isSame(self, p, q):
        if p is None and q is None:
            return True
        if p.val == q.val:
            return True
        else:
            return False


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.right = TreeNode(3)
    sol = Solution()
    res = sol.isSameTree(p, q)
    assert res == False
