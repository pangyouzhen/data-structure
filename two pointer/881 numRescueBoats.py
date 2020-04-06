from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        res = 0
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                res += 1
            else:
                right -= 1
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numRescueBoats([1, 2], 3))
    print(sol.numRescueBoats([3, 2, 2, 1], 3))
    print(sol.numRescueBoats([3, 5, 3, 4], 5))
    print(sol.numRescueBoats([2, 2], 6))
    print(sol.numRescueBoats([3, 2, 3, 2, 2], 6))
