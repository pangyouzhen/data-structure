from typing import List

# TODO 
class Solution:
    def maximumSubsequenceCount(self, text: str,pattern:str) -> int:
        pre = pattern[0] 
        res = []
        nums = 1
        for i in range(1,len(text)):
            if text[i] not in pattern:
                continue
            if text[i] != pre:
                # res.append(pre) 
                res.append(nums)
                nums = 1
                pre = text[i] 
            else:
                nums += 1
        # res.append(pre)
        res.append(nums)
        print(res)
        # print(res)
        even = 0
        
        for i,v in enumerate(res):
            if i % 2 == 1:
                even += v
                even += res[i-1] * v
        return even 
                

if __name__ =="__main__":
    func = Solution().maximumSubsequenceCount
    # text = "abdcdbc"
    # pattern = "ac"
    # text = "aabb"
    text = "zigfj"
    pattern = "ju"
    print(func(text,pattern))
