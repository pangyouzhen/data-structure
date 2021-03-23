#  二叉树：


# 二叉搜索树
#    左子树节点均小于根节点，右子树节点均大于根节点
#    各个子节点也是如此
# 特殊性质
#     二叉查找树的中序遍历是有序的
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list2(cls, nums: List[int], sort_bool=True) -> Optional["TreeNode"]:
        """
        从列表生成树，sort_bool=True 默认生成二叉搜索树
        """
        if sort_bool:
            nums.sort()
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = cls.from_list2(nums[:mid])
        root.right = cls.from_list2(nums[mid + 1:])
        return root

    #  中序遍历，只有二叉搜索树的中序遍历是有序的
    # TODO
    def simpleInorderBST(self, root: "TreeNode") -> List:
        if root:
            self.simpleInorderBST(root.left)
            yield str(root.val)
            self.simpleInorderBST(root.right)


if __name__ == '__main__':
    nums = [3, 2, 1, 4, 8, 5]
    sol = TreeNode.from_list2(nums)
    print("finish")