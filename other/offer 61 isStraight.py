from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        #  [1,2,3,4,5]
        #  [1,2,2,4,5]
        # [0,0,1,2,5]
        # [0,0,3,4,5]
        res = []
        for i in nums:
            if i != 0:
                res.append(i)
        if len(set(res)) != len(res):
            return False
        return (max(res) - min(res)) <= 4


if __name__ == '__main__':
    nums = [1, 2, 2, 0, 5]
    func = Solution().isStraight
    print(func(nums))
