class Solution:
    def removeDuplicates(self, nums):
        alpha = None
        alpha_num = 0
        start = 0
        while start < len(nums):
            if nums[start] != alpha:
                alpha = nums[start]
                alpha_num += 1
            else:
                del nums[start]
                start -= 1
            start += 1
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.removeDuplicates(nums))
    print(nums)