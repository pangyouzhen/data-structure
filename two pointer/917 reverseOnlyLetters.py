class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result = []
        for i in S:
            if i.isalpha():
                result.insert(0, i)
