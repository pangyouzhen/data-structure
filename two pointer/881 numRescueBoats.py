from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numberBoats = 0
        people.sort()
        i, j = 0, len(people)-1
        # Two pointer approach
        while i <= j:
            if (people[i] + people[j]) <= limit:
                i += 1
                j -= 1
                numberBoats += 1
            else:
                j -= 1
                numberBoats += 1
        return numberBoats

if __name__ == '__main__':
    sol = Solution()
    print(sol.numRescueBoats([1, 2], 3))
    assert  sol.numRescueBoats([3, 2, 2, 1], 3) == 3
    print(sol.numRescueBoats([3, 5, 3, 4], 5))
    print(sol.numRescueBoats([2, 2], 6))
    print(sol.numRescueBoats([3, 2, 3, 2, 2], 6))
