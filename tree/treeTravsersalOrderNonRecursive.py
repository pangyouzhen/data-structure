class ChildTreeNode:
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
    root = ChildTreeNode("A")
    root.child.append(ChildTreeNode("B"))
    root.child.append(ChildTreeNode("F"))
    root.child.append(ChildTreeNode("D"))
    root.child.append(ChildTreeNode("E"))
    root.child[0].child.append(ChildTreeNode('K'))
    root.child[0].child.append(ChildTreeNode('J'))
    root.child[2].child.append(ChildTreeNode("G"))
    root.child[3].child.append(ChildTreeNode("C"))
    root.child[3].child.append(ChildTreeNode("H"))
    root.child[3].child.append(ChildTreeNode("I"))
    root.child[0].child[0].child.append(ChildTreeNode("N"))
    root.child[0].child[0].child.append(ChildTreeNode("M"))
    root.child[3].child[0].child.append(ChildTreeNode("O"))
    root.child[3].child[2].child.append(ChildTreeNode("L"))
    treeNonRecusive = TreeNonRecursive()
    treeNonRecusive.travse_tree(root)