from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first_element = nums.index(target)
            end_element = len(nums) - nums[::-1].index(target) - 1
            result = [first_element, end_element]
        except ValueError:
            result = [-1, -1]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([5, 7, 9, 10], 8))
