from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        for i in range(max_num + 1):
            if i not in nums:
                return i
        return max_num + 1


if __name__ == '__main__':
    a = [0]
    sol = Solution()
    print(sol.missingNumber(a))
