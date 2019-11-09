# time out

class Solution:
    def countprimes(self, n):
        t = len(n)
        memo = [True] * (t + 1)
        memo[0], memo[1], memo[2] = False, False, False
        init = 2
        pass
        # ls = [2, ]
        # if n < 3:
        #     return 0
        # else:
        #     for i in range(3, n):
        #         if self.is_primes(i, ls):
        #             ls.append(i)
        return len(ls)

    def is_primes(self, n, ls):
        a = 0
        t = len(ls)
        while a < t:
            if n % ls[a] == 0:
                return False
            a = a + 1
        return True


if __name__ == '__main__':
    sol = Solution()
    # 2 [2]
    # 3/2 [2,3]
    # 4/2 [2,3]
    # 5/2,5/3 [2,3,5]
    # 6/2 ---[]
    # 7/2,7/3,7/5 [2,3,5,7]
    # [2,3,4,5,6,7,8,9,10]
    assert sol.countprimes(10) == 4
    assert sol.countprimes(8) == 4
    assert sol.countprimes(2) == 0
    assert sol.countprimes(3) == 1
    res = sol.countprimes(499979)
    print(res)
    # assert sol.isPrimes(1) == False
    # assert sol.isPrimes(2) == True
    # assert sol.isPrimes(3) == True
    # assert sol.isPrimes(4) == False
    # assert sol.isPrimes(5) == True
    # assert sol.isPrimes(6) == False
    # assert sol.isPrimes(7) == True
