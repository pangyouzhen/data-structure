class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        removed = set()
        res = 1
        ans = 1
        while res < n:
            print(removed)
            removed.add(target - res)
            res += 1
            ans += res
        return res

if __name__ == "__main__":
    func = Solution().minimumPossibleSum
    print(func(2,3))