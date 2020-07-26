# 二叉搜索树
# 左子树节点均小于根节点，右子树节点均大于根节点
#  各个子节点也是如此
# 特殊性质
# 二叉查找树的中序遍历是有序的
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self, nums):
        self.root = self.__sortedArrayToBST(nums)

    # 这个将已经排序的数组转为二叉搜索树，如果没排序的是不可以的
    def __sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.__sortedArrayToBST(nums[:mid])
        root.right = self.__sortedArrayToBST(nums[mid + 1:])
        return root

    def __repr__(self):
        res = []
        result = self.simpleInorder(self.root, res)
        return ",".join(result)

    def simpleInorder(self, root: TreeNode, res: List) -> List:
        if root:
            self.simpleInorder(root.left, res)
            res.append(str(root.val))
            self.simpleInorder(root.right, res)
        return res


if __name__ == '__main__':
    nums = [3, 2, 1, 4, 8, 5]
    nums.sort()
    sol = BST(nums)
    print(sol)
