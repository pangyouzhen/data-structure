from collections import Counter
from string import ascii_lowercase


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        reverse_lowercase = ascii_lowercase[::-1]
        c = Counter(s)
        ans = ""
        last = "#"
        reps = 0
        while True:
            flag = False
            # c++: for (int i=25;i>=0 && !flag;i--)
            for i in reverse_lowercase:
                if not flag:
                    if c[i] == 0:
                        continue
                    if i == last:
                        if reps + 1 <= repeatLimit:
                            ans += i
                            reps += 1
                            flag = True
                            c[i] -= 1
                    else:
                        ans += i
                        last = i
                        reps = 1
                        flag = True
                        c[i] -= 1
            #  如果尝试了26个字母都没有填成功,flag 代表填没填成功
            if not flag:
                break
        return ans


if __name__ == '__main__':
    s = "cczazcc"
    repeatLimit = 3
    sol = Solution()
    func = sol.repeatLimitedString
    print(func(s, repeatLimit))
