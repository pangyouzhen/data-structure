from typing import List


# TODO
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        half_sum = total_sum / 2
        if half_sum.is_integer():
            # 从n个数中凑成和为half sum的，不能重复的取，是一棵树，回溯
            # 对于list中的每一个元素，都有选择和不选择两种情况，有2^n 种情况，所以需要进行剪枝
            nums.sort()
            pass
        else:
            return False

    def conbine(self, nums, target):
        start = 0
        return self.conbine_memo(nums, target, start)

    def conbine_memo(self, nums, target, start):
        if target == 0:
            return True
        for i in range(start):
            target -= nums[i]
            if target < 0:
                return False
            self.conbine_memo(nums, target, start + 1)
            start += 1


#  这题

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    sol = Solution()
    print(sol.canPartition(nums))
    nums2 = [1, 2, 3, 5]
    print(sol.canPartition(nums2))
    nums3 = [1]
    print(sol.canPartition(nums3))
    nums4 = [3, 3, 3, 4, 5]
    print(sol.canPartition(nums4))
