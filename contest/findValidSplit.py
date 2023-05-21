import math
from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        l = len(nums)
        suffix_product_first = 1
        prefix_product_first = nums[0]
        for i in range(1, l):
            suffix_product_first *= nums[i]
        if math.gcd(suffix_product_first, prefix_product_first) == 1:
            return 0
        pointer = 1
        while pointer < l - 2:
            prefix_product_first = prefix_product_first * nums[pointer]
            suffix_product_first = suffix_product_first / nums[pointer]
            if math.gcd(prefix_product_first, int(suffix_product_first)) == 1:
                return pointer
            pointer += 1
        return -1


if __name__ == "__main__":
    func = Solution().findValidSplit
    nums = [4, 7, 8, 15, 3, 5]
    print(func(nums))
