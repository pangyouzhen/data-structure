class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for ind,(a,b,c,m) in enumerate(variables):
            if ((a**b % 10)**c) % m == target:
                res.append(ind)
        return res