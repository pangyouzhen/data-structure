from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k == 1:
            return -1
        elif len(nums) > 1 and k == 1:
            return nums[1]
        "k=2 only delete the first element"
        if k == 2:
            return nums[0]
        max_value = max(nums)
        ind = nums.index(max_value)
        if ind < k:
            return max_value
        else:
            return max(nums[:k+1])

if __name__ == "__main__":
    func = Solution().maximumTop
    nums = [35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49]
    k = 15
    assert func(nums, k) == 94