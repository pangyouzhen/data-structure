class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while (i < len(nums)):
            if nums[i] == 0:
                nums.pop(nums.index(0))
                nums.append(0)
            i = i + 1
        print(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 0, 3, 0, 12]
    # [0,1,0,3,12]
    # [1,0,3,12,0]
    # [1,3,12,0,0]
    res = sol.moveZeroes(nums)
    print(res)
