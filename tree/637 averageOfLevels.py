# Definition for a binary tree node.
from typing import List

a = [(3, 0), (9, 1), (20, 1), (15, 2), (7, 2)]
temp = 0
count = 0
val = 0
result = []
for i in range(0, len(a)):
    print(a[i])
    if a[i][1] == temp:
        count += 1
        val += a[i][0]
    elif a[i][1] != a[i - 1][1]:
        temp = a[i][1]
        result.append(val / count)
print(result)
print("-------------------------------------------")


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bfs(self, root: TreeNode):
        res, a = [], [(root, 0)]
        while a:
            fst, level = a.pop()
            res.append((fst.val, level))
            if fst.right:
                a.append((fst.right, level + 1))
            if fst.left:
                a.append((fst.left, level + 1))
        return res

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = self.bfs(root)

    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        def dfs(root: TreeNode, level: int):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        print(counts)
        print(totals)
        return [total / count for total, count in zip(totals, counts)]


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print(sol.bfs(tree))
    print(sol.averageOfLevels2(tree))
