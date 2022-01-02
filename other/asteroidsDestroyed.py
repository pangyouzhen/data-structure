from typing import List

class Solution():
    def asteroidsDestroyed(self, mass:int,asteroids: List) -> bool:
        asteroids.sort()
        l = len(asteroids)
        for i in range(l):
            if mass >= asteroids[i]:
                mass += asteroids
            else:
                return False
        return True

if __name__ =="__main__":
    func = Solution().asteroidsDestroyed
    nums =[]
    print(func(nums))