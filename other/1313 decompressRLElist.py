from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        start = 0
        while start < len(nums):
            temp = nums[start] * [nums[start + 1]]
            res.extend(temp)
            start += 2
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.decompressRLElist(nums))
