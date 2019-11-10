class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord("A") + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    # assert sol.titleToNumber("A") == 1
    print(sol.titleToNumber("A"))
