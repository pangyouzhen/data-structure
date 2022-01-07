from typing import List

class Solution():
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length = 0
        for i in sentences:
            l = len(i.split())
            if l > max_length:
                max_length = l
        return max_length

if __name__ =="__main__":
    func = Solution().mostWordsFound
    nums =[]
    print(func(nums))