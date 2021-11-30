class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        mid = len(s) / 2
        for i in range(int(mid)):
            element = s[:i+1]
            print(element)
            if s.replace(element, "") == "":
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    s = "babbabbabbabbab"
    print(sol.repeatedSubstringPattern(s))
