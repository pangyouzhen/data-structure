from typing import List
import sys

sys.set_int_max_str_digits(10**5)

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # 小于被除数的均为0
        # 切片耗时
        # return [1 if int(word[:i]) % m == 0 else 0 for i in range(1,len(word) + 1)]
        l  = len(word)
        res = []
        word = int(word)
        while word != 0:
            if word % m == 0:
                res.append(1)
            else:
                res.append(0)
            word = word // 10
            print(word)
        res.extend([0] * (l-len(res)))
        return res[::-1]
    
word = "86217457695827338571"
m = 8
func = Solution().divisibilityArray
print(func(word,m))