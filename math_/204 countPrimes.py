class Solution:
    # TODO
    def countPrimes(self, n):
        is_primes = [1 for i in range(n)]
        primes = [0 for i in range(n)]
        count = 0
        for i in range(2,n):
            if is_primes[i] == 1:
                primes[count] = i
                count += 1
            j = 0
            while primes[j] * i < n:
                is_primes[primes[j] * i] = 0
                if i % primes[j] == 0:
                    break
                j += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.countPrimes(10))
    # 2 [2]
    # 3/2 [2,3]
    # 4/2 [2,3]
    # 5/2,5/3 [2,3,5]
    # 6/2 ---[]
    # 7/2,7/3,7/5 [2,3,5,7]
    # [2,3,4,5,6,7,8,9,10]
    assert sol.countPrimes(10) == 4
    assert sol.countPrimes(8) == 4
    # assert sol.countprimes(2) == 0
    # assert sol.countprimes(3) == 1
    res = sol.countPrimes(499979)
    print(res)
