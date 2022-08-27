from typing import List

class Solution:
    def firstPalindrome(self, nums: List[str]) -> str:
        res = ""
        for num in nums:
            if self.isPaliddrome(num):
                return num
        return res

    def isPaliddrome(self,s:str):
        l =len(s)
        left = 0
        right = l -1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
         

if __name__ =="__main__":
    func = Solution().firstPalindrome
    nums = ["abc","car","ada","racecar","cool"]
    print(func(nums))