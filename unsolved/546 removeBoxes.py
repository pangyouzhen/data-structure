from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        for i in boxes:
            boxes = i ** 2
            self.removeBoxes()
