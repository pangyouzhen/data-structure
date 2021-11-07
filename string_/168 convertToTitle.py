class Solution:
    def convertToTitle(self, n: int) -> str:
        result, num = "", n
        while num:
            result += chr((num - 1) % 26 + ord("A"))
            num = (num - 1) // 26
        return result[::-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.convertToTitle(1) == "A"
