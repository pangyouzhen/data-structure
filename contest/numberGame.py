class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0,len(nums),2):
            s = nums[i:i+2]
            print(s)
            res.extend(s[::-1])
        return res