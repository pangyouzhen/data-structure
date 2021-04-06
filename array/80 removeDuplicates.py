from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = 0
        init_val = None
        i = 0
        while i < len(nums):
            val = nums[i]
            if val == init_val:
                m += 1
                if m >= 2:
                    del nums[i]
                    i -= 1
            else:
                init_val = val
                m = 0
            i += 1
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    sol.removeDuplicates(nums2)
    print(nums2)
