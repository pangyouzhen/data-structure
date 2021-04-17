from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        neg_num = 0
        for i in nums:
            if i < 0:
                neg_num += 1
        if neg_num % 2 == 1:
            return -1
        else:
            return 1


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, 3, 2, 1]
    sol = Solution()
    print(sol.arraySign(nums))
