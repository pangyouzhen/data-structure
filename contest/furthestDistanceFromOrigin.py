class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n1 = moves.count("L")
        n2 = moves.count("R")
        n3 = moves.count("_")
        return abs(n1 - n2) + n3