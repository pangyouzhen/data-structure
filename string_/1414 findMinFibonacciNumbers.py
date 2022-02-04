from typing import List
from bisect import bisect
class Solution():
    def findMinFibonacciNumbers(self, k:int) -> int:
        fibs = [1,1]
        while True:
            n = fibs[-1] + fibs[-2]
            if n > k:
                break
            else:
                fibs.append(n)
        t = 0
        while k not in fibs:
            ind = bisect(fibs,k)
            k = k - fibs[ind-1]
            # print(f"{fibs[ind-1]}")
            t += 1
        return t + 1
        
         

if __name__ =="__main__":
    func = Solution().findMinFibonacciNumbers
    nums = 19
    print(func(nums))