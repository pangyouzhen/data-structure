class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def dfs(root: TreeNode):
    stack = [root]
    while stack:
        temp = stack.pop()
        left = temp.left
        right = temp.right
        if right:
            stack.append(right)
        if left:
            stack.append(left)
        print(temp.val, end=" ")


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    bfs(tree)
    print("--")
    dfs(tree)
