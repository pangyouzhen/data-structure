from typing import List


class Solution:
    # 递归，而不是笛卡尔乘积，笛卡尔乘积只有两层
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute(n):
                result.append([num] + y)
        return result



if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
