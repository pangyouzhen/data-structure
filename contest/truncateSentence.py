class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        t = s.split(" ")
        return " ".join(t[:k])