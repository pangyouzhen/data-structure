class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        for i in range(N, 0, -1):
            if self.check_monotone(i):
                return i
        return 0

    def check_monotone(self, N: int):
        nums_str = str(N)
        for i, v in enumerate(nums_str[1:]):
            if int(nums_str[i + 1]) - int(nums_str[i]) >= 0:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums1 = 273070984
    print(sol.monotoneIncreasingDigits(nums1))
    # assert sol.monotoneIncreasingDigits(nums1) == 1234
    # nums2 = 322
    # assert sol.monotoneIncreasingDigits(nums2) == 299
    # nums3 = 10
    # assert sol.monotoneIncreasingDigits(nums3) == 9
