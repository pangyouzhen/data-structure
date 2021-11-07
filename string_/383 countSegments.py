class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSegments("                "))
