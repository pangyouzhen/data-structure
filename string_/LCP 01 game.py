from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        n = len(guess)
        start = 0
        result = 0
        while start < n:
            if guess[start] == answer[start]:
                result += 1
            start += 1
        return result
