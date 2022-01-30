from typing import List
from collections import defaultdict
from string import ascii_lowercase


class Solution():
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        ind = {v: i + 1 for i, v in enumerate(ascii_lowercase)}
        mod_val = []
        c = defaultdict(int)
        for i, v in enumerate(s):
            val = ind[v] * power ** c[v] % modulo
            c[v] += 1
            mod_val.append(val)
        print(mod_val)
        init_val = sum(mod_val[0:k])
        if init_val % modulo == hashValue:
            return s[0:k]
        for i in range(k, len(s) - k + 1):
            init_val = init_val + mod_val[i] - mod_val[i - k]
            # print(f"{i}", init_val)
            if init_val % modulo == hashValue:
                return s[i-k+1:i+1]


if __name__ == "__main__":
    func = Solution().subStrHash
    s ="xxterzixjqrghqyeketqeynekvqhc"
    power = 15
    modulo = 94
    k = 4
    hashValue = 16
    # s = "leetcode"
    # power = 7
    # modulo = 20
    # k = 2
    # hashValue = 0
    print(func(s, power, modulo, k, hashValue))
