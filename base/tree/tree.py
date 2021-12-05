from typing import List, Dict

# 广度优先遍历
from base.tree.tree_node import TreeNode


def bfs(root: TreeNode):
    queue = [root]
    while queue:
        temp = queue.pop(0)
        left = temp.left
        right = temp.right
        if left:
            queue.append(left)
        if right:
            queue.append(right)
        print(temp.val, end=" ")


def dfsPreorder(root: TreeNode):
    stack = [root]
    res = []
    while stack:
        temp = stack.pop()
        if temp:
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            res.append(temp.val)
    # 前序遍历先中间节点，然后左节点，然后右节点。因为是stack是先进后出，所以先把右节点的放进去
    return res


def dfsPostorder(root: TreeNode):
    stack = [root]
    res = []
    while stack:
        temp = stack.pop()
        if temp:
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            res.append(temp.val)
    # 后序遍历是先左节点，后右节点，最后中间节点，反过来一下就是先中间节点，然后右节点，再左节点，stack是先进后出，所以是先把左节点放进去
    return res[::-1]


# 后序是先left后倒排


def inorderTraversal(root: TreeNode) -> List[int]:
    stack, res = [], []

    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


# def inorderTraversalTest(root: TreeNode) -> List[int]:
#     stack, res = [root], []
#     # 中序是先左后中后右
#     while stack:
#         temp = stack.pop()
#         if temp:
#             if temp.left:
#                 stack.append(temp.left)
#                 res.append(temp.left.val)
#             if temp.right:
#                 stack.append(temp.right)
#             res.append(temp.val)
#     return res
def preorderNonRecursive(root: TreeNode) -> List[int]:
    if root is None:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return res


class Solution:

    def __init__(self):
        self.res = []

    def find_path(self, root: TreeNode, value: int):
        # 找到到value的路径，每个节点的值都不是相同的
        if root is None:
            return False
        self.res.append(root.val)
        if root.val == value:
            return True
        b = False
        if root.left is not None:
            b = self.find_path(root.left, value)
        if b is False and root.right is not None:
            b = self.find_path(root.right, value)
        if b is False:
            self.res.pop()
        return b

    def find_path2(self, root: TreeNode, value: int):
        self.res.append(root.val)
        if root.val == value:
            return True
        for i in [root.left, root.right]:
            if i:
                # self.res.append(i.val)
                b = self.find_path(i, value)
                if b is False:
                    self.res.pop()
                else:
                    break


if __name__ == '__main__':
    nums = "[6,8,4,9,7,3,5]"
    tree = TreeNode.from_strs(nums)
    print(tree)
    # print(bfs(tree))
    # print("---------")
    # print(dfs(tree))
    # print('---------')
    # print(f'inorder is {inorderTraversal(tree)}')
    # print(f'dfs preorder is {dfsPreorder(tree)}')
    # print(f'dfs postorder is {dfsPostorder(tree)}')
    # print(f'inorderTravsalTest is {inorderTraversalTest(tree)}')
    sol = Solution()
    # func = sol.find_path(tree, 9)
    func = sol.find_path2(tree, 9)
    print(sol.res)
    # print(preorderNonRecursive(tree))
