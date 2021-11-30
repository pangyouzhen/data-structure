from typing import List

from base.tree.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    nums = [3, 2, 1, 4, 5, 8]
    nums.sort()
    sol = Solution()
    a = sol.sortedArrayToBST(nums)
    print(a)