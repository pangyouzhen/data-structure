from typing import List
from itertools import permutations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        all_number = sorted(nums)
        next_flag = False
        change_flag = False
        for i in permutations(all_number, len(all_number)):
            if next_flag:
                nums = list(i)
                change_flag = True
                break
            if list(i) == nums:
                next_flag = True
        if not change_flag:
            nums = list(all_number)


if __name__ == "__main__":
    func = Solution().nextPermutation
    # nums = [1, 2, 3]
    nums = [3, 2, 1]
    func(nums)
    print(nums)
