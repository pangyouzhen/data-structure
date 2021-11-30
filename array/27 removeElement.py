class Solution:
    def removeElement(self, nums, val):
        a = 0
        while a < len(nums):
            if nums[a] == val:
                del nums[a]
                a = a - 1
            a = a + 1
        return len(nums)


if __name__ == '__main__':
    sol = Solution().removeElement
    assert sol([3, 2, 2, 3], 3) == 2
    assert sol([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
