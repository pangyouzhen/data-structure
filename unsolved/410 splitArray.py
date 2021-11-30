from typing import List
from pprint import pprint


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        pass

if __name__ == '__main__':
    sol = Solution()
    nums = [7, 2, 5, 10, 8]
    print(sol.splitArray(nums, 2))
    # 7 / 2,5,10,8 max(sum1,sum2) = 25
    # 7,2 / 5,10,8 max(sum1,sum2) = 23
    # 7,2,5 / 10,8  max(sum1,sum2)=18
    # 7,2,5,10 / 8 max = 24
    #  这个题目有递归的问题/，因为m是不确定的，分为三组呢
    nums2 = [1, 4, 4]
    print(sol.splitArray(nums, 3))
