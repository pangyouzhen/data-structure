from typing import List, Optional

from base.tree.tree_node import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        root = max(nums)
        ind = nums.index(root)
        left = nums[:ind]
        right = nums[ind+1:]
        tree = TreeNode(root)
        tree.left = self.constructMaximumBinaryTree(left)
        tree.right = self.constructMaximumBinaryTree(right)
        return tree


if __name__ == '__main__':
    func = Solution().constructMaximumBinaryTree
    nums = [3, 2, 1, 6, 0, 5]
    print(func(nums))
