from collections import Counter, defaultdict


class FrequencyTracker:
    def __init__(self):
        self.d1 = defaultdict(int)
        self.d = defaultdict(list)

    def add(self, number: int) -> None:
        self.d1[number] += 1
        self.d[self.d1[number]].append(number)

    def deleteOne(self, number: int) -> None:
        self.d1[number] -= 1
        try:
            self.d[self.d1[number]].remove(number)
        except Exception as e:
            pass
        if self.d1[number] <= 0:
            self.d1[number] == 0
        else:
            self.d[self.d1[number]].append(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.d.keys():
            return True
        return False


# ["FrequencyTracker","hasFrequency","hasFrequency","add","hasFrequency","hasFrequency","hasFrequency","deleteOne","hasFrequency"]
# [[],[1],[1],[7],[1],[1],[1],[7],[1]]
# [null,false,false,null,true,true,true,null,false]
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
