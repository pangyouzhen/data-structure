class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = [i.upper() for i in s]
        l = len(s)
        remainder = l % k
        res = []
        if not s:
            return ""
        if remainder == 0:
            for i in range(0, l, k):
                res.append("".join(s[i:i + k]))
                res.append("-")
        elif remainder != 0:
            res.append("".join(s[:remainder]))
            res.append("-")
            for i in range(remainder, l, k):
                res.append(''.join(s[i:i + k]))
                res.append("-")
        res.pop(-1)
        return "".join(res)


if __name__ == '__main__':
    S = "5F3Z-2e-9-w"
    K = 4
    # S = "2-4A0r7-4k"
    # K = 3
    func = Solution().licenseKeyFormatting
    print(func(S, K))
