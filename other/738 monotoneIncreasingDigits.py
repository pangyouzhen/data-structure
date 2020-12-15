class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 思路很简单 找到第一个下降点，然后后面的都变为9 但是注意往前推导的情况例如 332
        st = str(N)
        for i in range(len(st) - 1):
            if st[i] > st[i + 1]:
                while (i > 0 and st[i] == st[i - 1]):
                    i -= 1
                return int(st[:i + 1] + "".join("0" * (len(st) - i - 1))) - 1
        return N


if __name__ == '__main__':
    sol = Solution()
    nums1 = 273070984
    assert sol.monotoneIncreasingDigits(1234) == 1234
    nums2 = 332
    assert sol.monotoneIncreasingDigits(nums2) == 299
    nums3 = 10
    assert sol.monotoneIncreasingDigits(nums3) == 9
