class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []
        m = 1
        exclude_nums = set()
        while len(res) < n:
            if m not in exclude_nums:
                res.append(m)
            exclude_nums.add(k-m)
            m += 1
        print(res)
        return sum(res)
    
