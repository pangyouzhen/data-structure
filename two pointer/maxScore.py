from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        t = 0
        for i in nums:
            ans += i
            if ans <= 0:
                break
            t += 1
        return t
    
# [-687767,-860350,950296,52109,510127,545329,-291223,-966728,852403,828596,456730,-483632,-529386,356766,147293,572374,243605,931468,641668,494446]