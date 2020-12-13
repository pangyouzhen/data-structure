class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, -2, -4, 0]
    res = sol.containsDuplicate(nums)
    print(res)
