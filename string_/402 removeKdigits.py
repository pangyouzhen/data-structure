# 一般要想到 递增序列的问题
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        for i in range(k):
            stack.pop()
        return "".join(stack).lstrip("0") or '0'


if __name__ == '__main__':
    sol = Solution()
    num = "1432219"
    k = 3
    print(sol.removeKdigits(num, k))
