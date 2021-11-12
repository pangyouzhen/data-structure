from typing import List
from pysnooper import snoop


class Solution:
    @snoop()
    # 可以视为双端队列
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        for i in range(nums):
            pass


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 5]
    func = Solution().isStraight
    print(func(nums))
