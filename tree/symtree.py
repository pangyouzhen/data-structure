# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return root.right.val == root.left.val
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,0)
        for i in range(0,len(nums)):
            if nums[i+1] - nums[i]< 0:
                return i-1
        return len(nums)

if __name__ == '__main__':
    pass
