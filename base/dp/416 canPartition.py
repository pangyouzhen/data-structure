from typing import List


# 这是一个背包问题
# F(i,c) = F(i-1,c) || F(i-1,c -w(i))
class Solution:
    # TODO 分割问题
    def __init__(self):
        # 进行记忆化搜索
        #  -1 表示没有计算过,0 表示不可以填充，1表示可以填充
        self.memo = None

    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        half_sum = total_sum / 2
        if half_sum.is_integer():
            self.memo = [[-1] * len(nums) for _ in range(int(half_sum) + 1)]
            # 从n个数中凑成和为half sum的，不能重复的取，是一棵树，回溯
            # 对于list中的每一个元素，都有选择和不选择两种情况，有2^n 种情况，所以需要进行剪枝
            return self.try_partition(nums, len(nums) - 1, half_sum)
        else:
            return False

    def try_partition(self, nums, index, half_sum):
        if half_sum == 0:
            return True
        if half_sum < 0 or index < 0:
            return False
        if self.memo[index][half_sum] != -1:
            return self.memo[index][sum] == 1
        self.memo[index][half_sum] = (self.try_partition(nums, index - 1, half_sum) or self.try_partition(nums, index - 1, half_sum - nums[index]))
        return self.memo[index][half_sum] == 1


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
