class TreeNode:
    def __init__(self, key):
        self.key = key
        self.child = []


class TreeNonRecursive:

    def travse_tree(self, root):
        stack = []
        stack.append(root)
        while (len(stack)):
            curr = stack[0]
            stack.pop(0)

            print(curr.key, end=" ")
            for it in range(len(curr.child) - 1, -1, -1):
                stack.insert(0, curr.child[it])


if __name__ == '__main__':
    root = TreeNode("A")
    (root.child).append(TreeNode("B"))
    (root.child).append(TreeNode("F"))
    (root.child).append(TreeNode("D"))
    (root.child).append(TreeNode("E"))
    (root.child[0].child).append(TreeNode('K'))
    (root.child[0].child).append(TreeNode('J'))
    (root.child[2].child).append(TreeNode("G"))
    (root.child[3].child).append(TreeNode("C"))
    (root.child[3].child).append(TreeNode("H"))
    (root.child[3].child).append(TreeNode("I"))
    (root.child[0].child[0].child).append(TreeNode("N"))
    (root.child[0].child[0].child).append(TreeNode("M"))
    (root.child[3].child[0].child).append(TreeNode("O"))
    (root.child[3].child[2].child).append(TreeNode("L"))
    treeNonRecusive = TreeNonRecursive()
    treeNonRecusive.travse_tree(root)