import string


class Solution:
    def modifyString(self, s: str) -> str:
        lowcase = set('abcdefghijklmnopqrstuvwxyz')
        s_ = set(s)
        t = list(lowcase - s_)
        m = 0
        res = []
        for i in s:
            if i == "?":
                if m >= len(t):
                    m = 0
                res.append(t[m])
                m += 1
            else:
                res.append(i)
        return "".join(res)


if __name__ == '__main__':
    # s = "??yw?ipkj?"
    s = "v????gm??a?czgn?ba?dya?????b?t????j??ag??qm?????t?imx?f??gc??a????orb??e?uvae?ak?????a?e??f??qg"
    sol = Solution()
    print(sol.modifyString(s))
