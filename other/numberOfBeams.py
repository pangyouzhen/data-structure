from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ones = []
        for i,v in enumerate(bank):
            n = v.count("1")
            if n != 0:
                ones.append(n)
        if len(ones) == 1:
            return 0
        res = 0
        for t in range(len(ones)-1):
            res += ones[t] * ones[t+1]
        return res
                  

if __name__ =="__main__":
    func = Solution().numberOfBeams
    nums =[]
    print(func(nums))
