class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except Exception as e:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isNumber("12e"))
    print(sol.isNumber("0"))
