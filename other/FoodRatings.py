from typing import List
from heapq import heapify,heappush,heappop
from bisect import insort,bisect
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_country = {}
        self.cus_rating =  defaultdict(list)
        for i,v,j in zip(foods,cuisines,ratings):
            self.food_country[i] = v
            # insort(self.cus_rating[v],(i,j))
            # python 3.10 以上才支持
            insort(self.cus_rating[v],(i,j),key=lambda x:(x[1],x[0]))
              

    def changeRating(self, food: str, newRating: int) -> None:
        pass


    def highestRated(self, cuisine: str) -> str:
        pass


if __name__ == "__main__":
    food = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
    print(food.food_country)
    print(food.cus_rating)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)