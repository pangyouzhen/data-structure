class Solution:
    def removeDuplicates(self, nums):
        a = []
        i = 0
        while (i < len(nums)):
            if nums[i] in a:
                nums.pop(i)
                i = i - 1
            else:
                a.append(nums[i])
            i = i + 1
        return len(set(nums))


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    len_nums = sol.removeDuplicates(nums)
    for i in range(len_nums):
        print(nums[i])
