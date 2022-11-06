from typing import List

class Solution:
    def continue_nums(self, text: List[str]) -> str:
        pre = text[0] 
        res = []
        nums = 1
        for i in range(1,len(text)):
            if text[i] != pre:
                res.append(pre) 
                res.append(str(nums))
                nums = 1
                pre = text[i] 
            else:
                nums += 1
        res.append(pre)
        res.append(nums)
        return res

if __name__ =="__main__":
    func = Solution().continue_nums
    nums = "abbcdeebb"
    nums2 = "a" 
    print(func(nums))
    print(func(nums2))