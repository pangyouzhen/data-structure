from typing import List

from base.tree.tree_node import TreeNode


def bfs(root: TreeNode):
    #  b
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

if __name__ == '__main__':
    tree = TreeNode(6)
    tree.left = TreeNode(8)
    tree.right = TreeNode(4)
    # tree.left.left = TreeNode(9)
    # tree.left.right = TreeNode(7)
    # tree.right.left = TreeNode(5)
    # tree.right.right = TreeNode(3)
    print(bfs(tree))
    print("---------")
    print(dfs(tree))
    print('---------')
    print(f'inorder is {inorderTraversal(tree)}')
    print(f'dfs preorder is {dfsPreorder(tree)}')
    print(f'dfs postorder is {dfsPostorder(tree)}')
    # print(f'inorderTravsalTest is {inorderTraversalTest(tree)}')