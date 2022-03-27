import string

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dic = {v: str(i + 1) for i, v in enumerate(string.ascii_lowercase)}
        num_init = ""
        for i in s:
            num_init += dic[i]
        val = 0
        while k > 0:
            val = 0
            for i in num_init:
                val += int(i)
            num_init = str(val)
            k -= 1
        return val


if __name__ == '__main__':
    s = "iiii"
    k = 1
    # s = "leetcode"
    # k = 2
    sol = Solution()
    print(sol.getLucky(s, k))
