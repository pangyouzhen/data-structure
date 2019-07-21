# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        else:
            return self.isSameTreeRec(p,q)
        # 一个成熟的coder必须考虑到各种异常的情况.和如何进行扩展

    def isSameTreeRec(self, p, q):
        output = False
        if p is None and q is None:
            output = True
        if p is not None and q is not None and p.val == q.val:
            output = True
        return output


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode
    q.right = TreeNode(3)
    sol = Solution()
    res = sol.isSameTree(p, q)
    assert res == False
