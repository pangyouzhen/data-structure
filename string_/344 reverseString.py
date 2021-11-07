class Solution:
    def reverseString(self, s):
        i = len(s)
        while (i > 0):
            # s.append(s[0])
            s.insert(i, s[0])
            s.pop(0)
            i = i - 1


if __name__ == '__main__':
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    res = sol.reverseString(s)
    print(res)
