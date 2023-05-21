import bisect
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = set("aeiou")
        
        ind = [i for i,v in enumerate(words) if ((v[-1] in s) and (v[0] in s))]
        print(ind)
        res = []
        for i in queries:
            right_ind = bisect.bisect(ind,i[-1])
            left_ind = bisect.bisect_left(ind,i[0])
            res.append(right_ind - left_ind)
        return res
            
        