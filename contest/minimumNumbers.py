from itertools import permutations

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num < k:
            return 0
        nums = []
        for i in range(k,num+1,10):
            nums.append(i)
        t = [k*i for i in range(10)]
        res = []
        # print(t)
        for ts in t:
            if num >= ts:
                if (num - ts)%10 == 0:
                    val = ts / k
                    res.append(val)
        # print(res)
        if not res:
            return -1
        for r in res:
            for t in permutations(nums,int(r)):
                print(t)
                if sum(t) == num:
                    return int(r)
        return -1

if __name__ == "__main__":
    func = Solution().minimumNumbers
    num = 10
    k = 0
    print(func(num,k))