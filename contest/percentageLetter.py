class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        t = s.count(letter)
        return int(t / len(s) * 100)


if __name__ == "__main__":
    func = Solution().percentageLetter
    nums = []
    print(func(nums))
