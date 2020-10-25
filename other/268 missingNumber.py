from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        max_num = max(nums)
        for i in range(max_num + 1):
            if i not in nums:
                return i
        return max_num + 1


#  in, not in, 这个函数比起相等比较费时,
if __name__ == '__main__':
    a = [3, 0, 1]
    sol = Solution()
    print(sol.missingNumber(a))
