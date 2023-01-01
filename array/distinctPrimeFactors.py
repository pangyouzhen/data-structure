from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def isPrime(n):
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        # print(isPrime(2))
        all_prime = [i for i in range(2,1000) if isPrime(i)]
        # print(all_prime)
        n = 0
        res = []
        for i in all_prime:
            for j in nums:
                if j % i == 0:
                    res.append(i)
                    continue
        # print(res)
        return len(set(res))

if __name__ == "__main__":
    func = Solution().distinctPrimeFactors
    nums = [2,4,3,7,10,6]
    print(func(nums))