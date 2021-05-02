class Solution:
    def splitString(self, s: str) -> bool:

        for i in range(1, len(s) - 1):
            val = int(s[:i])
            m = s
            while m:
                ind, is_val = self.is_zero(s, m, val - 1)
                if m:
                    pass
                else:
                    break
        return False

    def is_zero(self, s, m, val):
        val = str(val)
        if val in m:
            ind = m.index(val)
            return m, ind, True
        return False, False, False


if __name__ == '__main__':
    s = "10009998"
    val = 100
    m = "09998"
    sol = Solution()
    print(sol.is_zero(s, m, val))
